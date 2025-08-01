from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Django, this is app3')
# Create your views here.
