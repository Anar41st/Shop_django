from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('iphone15', views.iphone15, name='ip15'),
    path('iphone14', views.iphone14, name='ip14'),
    path('iphone13', views.iphone13, name='ip13'),
    path('iphone11', views.iphone11, name='ip11'),
    path('order', views.order, name='order'),
]