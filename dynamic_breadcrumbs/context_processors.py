from dynamic_breadcrumbs.utils import Breadcrumbs


def breadcrumbs(request):
    """
    Add breadcrumbs dict to the context.
    """
    base_url = request.build_absolute_uri("/")
    breadcrumbs = Breadcrumbs(base_url=base_url, path=request.path)
    return {"breadcrumbs": breadcrumbs.as_list()}
