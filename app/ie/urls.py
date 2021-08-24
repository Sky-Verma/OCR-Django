from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('img-to-txt/',views.img_to_txt,name='img-to-txt')
    ]