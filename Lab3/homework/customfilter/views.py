from django.shortcuts import render
# Create your views here.
def home(request):

    return render(request,'home.html')

def custom_filter(request):

    return render(request,'test_my_custom_filters.html')