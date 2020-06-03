from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def about(request):
    return render(request, 'main/about.html')


@login_required
def dash(request):
    return render(request, 'profiles/dashboard.html')
