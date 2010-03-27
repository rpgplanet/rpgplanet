from djangomarkup.models import SourceText, TextProcessor

from ella.core.models.main import Category, Author, Source
from ella.articles.models import Article, ArticleContents

from django.core.urlresolvers import reverse
from django.db.transaction import commit_on_success
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.contenttypes.models import ContentType


from django.template.defaultfilters import slugify
from zapisnik.forms import ArticleForm

from tagging.models import Tag

DEFAULT_TEXT_PROCESSOR = u'czechtile'

def home(request, template="zapisnik/home.html"):
    return direct_to_template(request, template, {})

@commit_on_success
def new(request, template="zapisnik/new.html"):
    article_form = None

    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            proc = TextProcessor.objects.get(name=DEFAULT_TEXT_PROCESSOR)

            category, created = Category.objects.get_or_create(
                title = "Main",
                slug = "main",
                tree_path = "",
                site = request.site
            )

            author, created = Author.objects.get_or_create(
                user = request.user,
                name = request.user.username,
                slug = slugify(request.user.username)
            )
            
            article = Article.objects.create(
                # updated = datetime.now()
                description = article_form.cleaned_data['annotation'],
                content_type = ContentType.objects.get_for_model(Article),
                category = category
            )
            article.authors.add(author)

            article.save()

            content = ArticleContents.objects.create(
                article = article,
                title = article_form.cleaned_data['title'],
                content = article_form.cleaned_data['content']
            )

            SourceText.objects.create(
                processor = proc,
                content_type = ContentType.objects.get_for_model(ArticleContents),
                object_id = content.pk,
                field = 'content'
            )

            Tag.objects.update_tags(article, article_form.cleaned_data['tags'])

            return HttpResponseRedirect(reverse("zapisnik-home"))

    if not article_form:
        article_form = ArticleForm()

    # add category (root on user site)
    # add author (owner of the site)
    # add placement wrrking
    # ? add placement (dilna)

    return direct_to_template(request, template, {
        'article_form' : article_form,
    })
