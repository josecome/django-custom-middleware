from django.http import HttpResponse

# Create your views here.

def home_view(request):
    result = f"Welcome! <br />Your Category is: { request.category }"
    return HttpResponse(
        f'<h1>{result}</h1>'
        )
    