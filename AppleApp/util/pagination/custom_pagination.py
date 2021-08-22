from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    page_size = 20
    max_page_size=100
    page_query_param = "page"
    page_size_query_param = "per_page"
