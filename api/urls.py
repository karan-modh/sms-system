from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', apiLogin),
    path('display/', display),
    path('logout/', apiLogout)
]
