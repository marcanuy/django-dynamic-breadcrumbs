from dynamic_breadcrumbs.utils import Breadcrumbs


def breadcrumbs(request):
    """
    Add breadcrumbs dict to the context.
    """
    breadcrumbs = Breadcrumbs(
        base_url=request.build_absolute_uri("/"), path=request.path
    )

    # Return a dictionary with the breadcrumbs data
    return {"breadcrumbs": breadcrumbs.as_list()}
