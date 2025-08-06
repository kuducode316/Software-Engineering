from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('custom_filter/', views.custom_filter, name='custom_filter'),
]