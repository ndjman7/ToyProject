from django.contrib.auth import authenticate, login as auth_login,\
    logout as auth_logout
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('blog:index')
        return redirect('user:login')


def logout(request):
    auth_logout(request)
    return redirect('blog:index')
