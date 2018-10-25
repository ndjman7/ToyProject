from django.contrib.auth import authenticate, login as auth_login,\
    logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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


@login_required
def logout(request):
    auth_logout(request)
    return redirect('blog:index')


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('blog:index')
        return render(request, 'registration/signup.html', {'form': form})
