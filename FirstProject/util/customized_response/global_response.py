ADD = "ADD"
MODIFY = "MODIFY"
DELETE = "DELETE"


class ResponseFomatter(object):

    @staticmethod
    def get_normal_response(data="", process_type="QUERY"):
        if process_type.upper() not in ["ADD", "MODIFY", "DELETE"]:
            data = data
        else:
            data = "{} SUCCESS".format(process_type.upper())
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
