from django.conf import settings
from rest_framework.pagination import PageNumberPagination

from FirstProject.util.customized_response.global_response import ResponseFomatter


class CustomPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_query_param = "page"
    page_size_query_param = "per_page"

    def get_my_next(self):
        return settings.SERVER_NAME + self.request.path + self.get_next_link().split(self.request.path)[1]

    def get_my_pre(self):
        return settings.SERVER_NAME + self.request.path + self.get_previous_link().split(self.request.path)[1]

    def get_paginated_response(self, data):
        response_data = ResponseFomatter.get_normal_response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
        return response_data
