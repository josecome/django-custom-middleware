class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.category = None
        age = request.GET.get('age')
        if int(age) < 18:
            request.category = 'Child'
        else:
            request.category = 'Adult'
                
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response