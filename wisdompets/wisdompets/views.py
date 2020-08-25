from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("<h2>This is the about page</h2>")
