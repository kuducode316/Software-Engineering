from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('Students_Table/',views.page,name='Students_Table'),
    path('all/',views.read,name='students'),
    path('read_one/',views.read_one,name='one_student'),
    path('create/',views.create,name='NewStudent'),
    path('update/',views.update,name='UpadateStudent'),
    path('delete/',views.delete,name='DeleteStudent'),

]

