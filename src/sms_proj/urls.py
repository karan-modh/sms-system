"""sms_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from accounts.views import UserRegisterFormView, LoginView, user_logout
from main.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', UserRegisterFormView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', user_logout, name='logout'),
    url(r'^/*', include('main.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
