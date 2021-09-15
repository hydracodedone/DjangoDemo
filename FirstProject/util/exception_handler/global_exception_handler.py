import logging
import traceback

from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler

from FirstProject.util.customized_response.global_response import ResponseFomatter
from FirstProject.util.logging.golobal_logging import MyAbstractLogger

LOGGER = logging.getLogger("error")



def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        LOGGER.error(
            "Request URL Is : {}, View Is : {}, Exception Is : {}".format(
                context["request"]._request.build_absolute_uri(),
                context["view"].__class__,
                exc
            )
        )
        LOGGER.error(traceback.format_exc())
        return Response(ResponseFomatter.get_unknown_error(exc.__str__()), status=HTTP_500_INTERNAL_SERVER_ERROR)
    return response
