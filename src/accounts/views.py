from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


@login_required
def special(request):
    return HttpResponse("You are Logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        prof_form = UserRegisterForm(data=request.POST)
        if user_form.is_valid() and prof_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = prof_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, prof_form.errors)
    else:
        user_form = UserForm()
        prof_form = UserRegisterForm()
    return render(request, 'main/signup.html', {'user_form': user_form, 'prof_form': prof_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Account was inactive !")
        else:
            print("Someone tried to login and failed.")
            print("They used username : {} and password : {}.".format(username, password))
            return HttpResponse("Invalid Login Details given")
    else:
        return render(request, 'main/login.html', {})
