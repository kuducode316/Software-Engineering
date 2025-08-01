from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Django, this is app1')
# Create your views here.
