from django.http import HttpResponse


def hello(request):
    return HttpResponse("This is in scheduler")

