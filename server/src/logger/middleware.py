import time
import datetime
from django.core.cache import cache
from .models import VisitModel
from settings.cache import CACHE_TTL

class RequestTimeMiddleware:
    def __init__(self, get_response):
       self.get_response = get_response

    def __call__(self, request):
        timestamp = time.monotonic()
        now = datetime.datetime.now()

        response = self.get_response(request)

        if not request.user.is_anonymous:
            data = {
                "url":request.path,
                "user":request.user.email,
                "start_at": now,
                "execution_time": f'{time.monotonic() - timestamp:.3f}s',
                "http_user_agent":request.META["HTTP_USER_AGENT"],
            }

            if 'logger2' in cache:
                loggers = cache.get('logger2')
                print([*loggers])
                cache.set('logger2', [data, *loggers], CACHE_TTL)
            else:
                cache.set('logger2', [data], CACHE_TTL)


            # model = VisitModel(data)
            # model.save()

        return response

        

