from ella.core.views import CategoryDetail

class SubdomainCategoryDetail(CategoryDetail):
    def get_context(self, request, category=None):
#        if category:
#            cat = get_cached_object_or_404(Category, tree_path=category, site__id=settings.SITE_ID)
#        else:
#            cat = get_cached_object_or_404(Category, tree_parent__isnull=True, site__id=settings.SITE_ID)
#        context = {
#                    'category' : cat,
#                    'is_homepage': not bool(category),
#                    'archive_entry_year' : self._archive_entry_year(cat),
#                }
        return super(SubdomainCategoryDetail, self).get_context(request, category)


home = category_detail = CategoryDetail()
