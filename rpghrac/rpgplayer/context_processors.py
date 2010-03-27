
def is_site_owner(request):
    return {'is_site_owner' : request.site_owner == request.user }
