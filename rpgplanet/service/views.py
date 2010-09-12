from django.http import Http404
from django.views.generic.simple import direct_to_template

from rpgcommon.user.models import UserProfile

def user_profile(request, user_slug, template='user/profile.html'):
    try:
        profile = UserProfile.objects.select_related().get(slug=user_slug)
    except UserProfile.DoesNotExists:
        raise Http404()

    return direct_to_template(request, template,
        {
            'displayed_user' : profile.user,
            'user_profile' : profile
        }
    )


def tos(request, template='tos.html'):
    return direct_to_template(request, template,
        {
        }
    )
