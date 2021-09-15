import logging

from django.db import connection
from django.utils.deprecation import MiddlewareMixin

LOGGER = logging.getLogger("sql")


class GlobalSqlMiddleWare(MiddlewareMixin):
    def process_response(self, request, response):
        request_url = request.build_absolute_uri(),
        query_sql = connection.queries
        if query_sql:
            LOGGER.info("Request URL Is : {}, SQL Is : \n{}\n".format(request_url, query_sql))
        return response
