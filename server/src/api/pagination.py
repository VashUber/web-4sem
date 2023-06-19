from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "per_page": self.page_size,
                "data": data,
            }
        )
