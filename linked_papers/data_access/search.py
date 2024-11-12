from django.core.paginator import Paginator, EmptyPage
from ..models import Essay
import faiss


def fetch(keyword, page):
    # 1. 查询包含关键词的论文数据
    papers = Essay.objects.filter(title__icontains=keyword).order_by('id')  # 假设是根据标题搜索，具体根据字段调整

    # 2. 设置分页，每页10条数据
    paginator = Paginator(papers, 10)  # 每页10条
    try:
        papers_page = paginator.page(page)  # 获取当前页的数据
    except EmptyPage:
        papers_page = paginator.page(paginator.num_pages)  # 如果请求页数超出范围，返回最后一页

    # 3. 返回分页后的数据
    papers_data = list(
        papers_page.object_list.values('title', 'abstract', 'publish_year', 'category'))  # 根据你的表结构返回需要的字段

    return {
        'papers': papers_data,
        'page': papers_page.number,
        'num_pages': paginator.num_pages
    }
