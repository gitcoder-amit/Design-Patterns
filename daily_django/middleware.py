def custommiddleware(get_response):  # get_response is an callable every request passed through this
    def middleware(request):
        resp = get_response(request)
        return resp

    return middleware


class CustomMiddleware(self):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resp = self.get_response(request)
        return resp