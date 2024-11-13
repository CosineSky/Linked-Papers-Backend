from django.core.paginator import Paginator, EmptyPage
from ..models import Essay


def fetch(essayId, page):
    # Search by categories
    category = Essay.objects.get(id=essayId).category
    essays = Essay.objects.filter(category=category).exclude(id=essayId)

    # Use paginator, 16 papers per page
    paginator = Paginator(essays, 16)
    try:
        papers_page = paginator.page(page)
    except EmptyPage:
        papers_page = paginator.page(paginator.num_pages)

    # Return data
    essays_data = list(
        papers_page.object_list.values('title', 'publish_year', 'category'))
    return {
        'papers': essays_data,
        'page': papers_page.number,
        'num_pages': paginator.num_pages
    }