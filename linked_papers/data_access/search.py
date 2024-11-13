from django.core.paginator import Paginator, EmptyPage
from ..models import Essay


def fetch(keyword, page):
    # Search by titles
    papers = Essay.objects.filter(title__icontains=keyword).order_by('id')

    # Use paginator, 8 papers per page
    paginator = Paginator(papers, 8)
    try:
        papers_page = paginator.page(page)
    except EmptyPage:
        papers_page = paginator.page(paginator.num_pages)

    # Return data
    papers_data = list(
        papers_page.object_list.values('title', 'publish_year', 'category'))
    return {
        'papers': papers_data,
        'page': papers_page.number,
        'num_pages': paginator.num_pages
    }
