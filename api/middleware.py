from django.utils.deprecation import MiddlewareMixin

class IPAddressMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            ip_addr = request.META.get('REMOTE_ADDR')
            if request.path == '/api/login/' and request.method == 'POST':
                if request.user.last_login_ip != ip_addr:
                    request.user.last_login_ip = ip_addr
                    request.user.save()

        response = self.get_response(request)
        return response

