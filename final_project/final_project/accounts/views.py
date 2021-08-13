from django.shortcuts import render, redirect, reverse
from .forms import CreateAccountForm, LoginForm
from .models import Account
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.


def register_view(request):
    context = {}
    #if request.user.is_authenticated:
    #    return redirect('')

    form = CreateAccountForm()
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        print('123')
        if form.is_valid():
            print('234')
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, 'Account created: ' + name)
            return redirect('login')
    else:
        context['form'] = form
        return render(request, 'register.html', context)


def login_view(request):
    context = {}

    form = LoginForm()
    if request.POST:
        print('abcabcbac')

        form = LoginForm(request.POST)
        if 'Register' in request.POST:
            return HttpResponseRedirect(reverse('register'))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                account = Account.objects.get(username=username, password=password)
            except Account.DoesNotExist:
                account = None
            if account is None:
                return HttpResponseRedirect(reverse('register'))
            return HttpResponseRedirect(reverse('home'))

    context['form'] = form
    return render(request, 'login.html', context)


def home_view(request):
    context = {}
    return render(request, 'home.html', context)
