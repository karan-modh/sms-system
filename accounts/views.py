from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView as DefaultLoginView
from .forms import UserRegisterForm
from django.views.generic import CreateView
from .models import UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
class LoginView(DefaultLoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super().get_redirect_url()
        return "/"


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserRegisterFormView(CreateView):
    model = UserProfile
    form_class = UserRegisterForm
    template_name = 'main/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        user = form.save()
        UserRegisterFormView.create_profile(user, **form.cleaned_data)
        return super(UserRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        userprofile = UserProfile.objects.create(user=user,
                                                 phone=kwargs['phone'],
                                                 company=kwargs['company'],
                                                 position=kwargs['position'])
        userprofile.save()