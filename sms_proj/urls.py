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
from .settings import MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from main.views import index, pricing, about, dash, FileUploadView, FormDisplayView

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('pricing', pricing, name='pricing'),
    path('about', about, name='about'),
    path('profile/details', dash, name='dash'),
    path('send-msg/', FileUploadView, name='send_msg'),
    path('gen-msg/', FormDisplayView, name='gen_msg'),
    # path('api/msg/', GenMessageView.as_view(), name='upload_msg'),
    path('account/', account_view, name="account"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, name="register"),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('', include('main.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
