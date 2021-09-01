from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):     #request als Standardvar, denn es handelt sich hier um spezifische Requests
    return render(request, "hello/index.html")

def nam(request):
    return HttpResponse("Hello, Nam")

def greet(request, name):
    return HttpResponse("Hello, {}".format(name))