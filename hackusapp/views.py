from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from django.contrib.auth.models import User

from .models import Challenge
from accounts.models import Member



# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        username = request.user
    else:
        username = request.user.username
    return render(request, 'home.html', {'username': username})

def challenge(request):
    challenge = Challenge.objects
    return render(request, 'challenge.html', {'challenge':challenge})

def introduce(request):
    return render(request, 'introduce.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def writeupboard(request):
    return render(request, 'writeupboard.html')

def ctf(request):
    return render(request, 'ctf.html')


def mypage(request):
    if  request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else: 
        data = {'username':"로그인이 필요합니다"}
    return render(request, 'mypage.html', {'data': data})