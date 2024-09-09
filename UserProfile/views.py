from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def register(request):
    return HttpResponse(f"<h1>Try to register user with name {request.GET['name']}, age:{request.GET['age']}</h1>")


def userId(request, userid):
    return HttpResponse(f"<h1>This pages about user № {userid}</h1>")
