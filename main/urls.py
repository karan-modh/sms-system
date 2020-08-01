from django.urls import path, include
from .views import index, pricing, about, dash
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    path('pricing', pricing, name='pricing'),
    path('about', about, name='about'),
    path('profile/details', dash, name='dash'),
    path('', index, name='index'),
]
