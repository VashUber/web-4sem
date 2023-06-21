from celery import shared_task
from django.core.cache import cache
from .serializers import VisitSerializer
from .models import VisitModel

@shared_task
def SaveLogger():
  cache_data = cache.get('logger2')
  # print(';tes', cache_data)
  if cache_data is not None:
    model2 = VisitSerializer(data=cache_data, many=True)

    if model2.is_valid():
      model2.save()
  
  cache.delete('logger2')

