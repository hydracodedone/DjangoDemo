from user_agents import parse


class CustomRequstAnalysor(object):

    @staticmethod
    def get_request_ip(request):
        ip = getattr(request, 'request_ip', None)
        if ip:
            return ip
        ip = request.META.get('REMOTE_ADDR', '')
        if not ip:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = 'unknown'
        return ip

    @staticmethod
    def get_browser(request):
        ua_string = request.META['HTTP_USER_AGENT']
        user_agent = parse(ua_string)
        return user_agent.get_browser()

    @staticmethod
    def get_os(request):
        ua_string = request.META['HTTP_USER_AGENT']
        user_agent = parse(ua_string)
        return user_agent.get_os()
