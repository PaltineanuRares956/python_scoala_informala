from django.shortcuts import render, redirect, reverse
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

# Create your views here.


def register_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('')

    form = CreateUserForm()
    if request.method == "POST":

        if 'Login' in request.POST:
            return HttpResponseRedirect(reverse('login'))

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Account created')
            return HttpResponseRedirect(reverse('login'))

    context['form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    context = {}

    form = LoginForm()
    if request.POST:

        if 'Register' in request.POST:
            return HttpResponseRedirect(reverse('register'))

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = authenticate(request, username=username, password=password)

            if account is None:
                messages.error(request, 'Username or password incorrect')
                return HttpResponseRedirect(reverse('login'))
            login(request, account)
            return HttpResponseRedirect(reverse('home'))

    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def home_view(request):
    return render(request, 'home.html', {})
