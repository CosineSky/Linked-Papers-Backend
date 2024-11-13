from django.core.exceptions import ObjectDoesNotExist
from ..models import Essay


def fetch(essayId):
    try:
        essay = Essay.objects.get(id=essayId)
        return {
            'title': essay.title,
            'abstract': essay.abstract,
            'publish_year': essay.publish_year,
            'category': essay.category,
        }
    except ObjectDoesNotExist:
        return None
