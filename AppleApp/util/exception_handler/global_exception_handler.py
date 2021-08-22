import traceback

from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler

from AppleApp.util.util import get_final_response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        print(
            "Request URL Is : {}, View Is : {}, Exception Is : {}".format(
                context["request"]._request.build_absolute_uri(),
                context["view"].__class__,
                exc
            )
        )
        print(traceback.format_exc())
        return Response(get_final_response(exc), status=HTTP_500_INTERNAL_SERVER_ERROR)
    return response
