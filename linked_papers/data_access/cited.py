from django.core.exceptions import ObjectDoesNotExist
from ..models import Essay, Edge


def fetch(essayId):
    cited_ids = Edge.objects.filter(essay_id=essayId).values_list('cited_id', flat=True)
    cited_essays = []
    for cited_id in cited_ids:
        try:
            cited_essay = Essay.objects.get(id=cited_id)
            cited_essays.append({
                'title': cited_essay.title,
                'publish_year': cited_essay.publish_year,
                'category': cited_essay.category,
            })
        except ObjectDoesNotExist:
            return None

    return cited_essays
