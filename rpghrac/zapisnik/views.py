from django.views.generic.simple import direct_to_template

from zapisnik.forms import ArticleForm

def home(request, template="zapisnik/home.html"):
    return direct_to_template(request, template, {})

def new(request, template="zapisnik/new.html"):
    article_form = ArticleForm()

    # add category (root on user site)
    # add author (owner of the site)
    # add placement wrrking
    # ? add placement (dilna)

    return direct_to_template(request, template, {
        'article_form' : article_form,
    })
