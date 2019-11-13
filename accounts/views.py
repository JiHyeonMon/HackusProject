from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['id'], 
                password = request.POST['password1']
                )
            nickname = request.POST['nickname']
            email = request.POST['email']
            member = Member(user=user, nickname = nickname, email=email)
            member.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username = id, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error' : 'id or password is incorrect.'})
    else:        
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')