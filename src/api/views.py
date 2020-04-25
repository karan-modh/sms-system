from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from accounts.models import UserProfile
from django.core import serializers
from django.contrib.auth.models import User
from django.middleware.csrf import *


# Create your views here.
def apiLogin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/api/login/')
        else:
            return HttpResponse("ERROR:-Credentials are Incorrect")
    else:
        if request.session.is_empty():
            return render(request, 'api/api_login_workThrough.html', {})
        authenticate(request)
        print('-------------------')
        print(request.user)
        return redirect('/api/index/')


def display(request):
    if request.method == 'GET':
        user = User.objects.filter(pk=request.user.pk)[0]
        profile = UserProfile.objects.filter(user=request.user.pk)[0]
        return HttpResponse(serializers.serialize('json', [user, profile]))


def apiLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse("ERROR:-Error Logging Out")
