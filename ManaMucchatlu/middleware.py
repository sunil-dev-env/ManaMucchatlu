from django.shortcuts import redirect

class NicknameMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.COOKIES.get('nickname') and not request.path.startswith('/nickname/'):
            return redirect('nickname')
        response = self.get_response(request)
        return response
