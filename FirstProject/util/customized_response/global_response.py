class ResponseFomatter(object):

    @staticmethod
    def get_normal_response(data):
        return {
            "msg": "handle success",
            "err": "",
            "data": data
        }

    @staticmethod
    def get_validated_error(err):
        return {
            "msg": "validate fail",
            "err": err,
            "data": "",
        }

    @staticmethod
    def get_unknown_error(err):
        return {
            "msg": "uncaptured error",
            "err": err,
            "data": ""
        }
