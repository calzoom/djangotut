from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views are Python functions that receive
# HttpRequest objects and return HttpResponse objects

# Receive a request as a parameter and return a response as a result
def home(reqeust):
    return HttpResponse('Hello, World!')
