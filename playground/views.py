from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
# request => response
# Request handler

def say_hello(request):
    # Pull data from db
    # return HttpResponse("Hello world")
    return render(request, 'hello.html', {'name': 'Evans'})
