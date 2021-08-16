from django.shortcuts import render, redirect, reverse
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth import views, authenticate

# Create your views here.


def register_view(request):
    logout(request)
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
            return redirect('login')

    context['form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    logout(request)
    context = {}

    form = LoginForm()
    if request.POST:
        if 'Register' in request.POST:
            return HttpResponseRedirect(reverse('register'))
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # try:
            #     account = User.objects.get(username=username, password=password)
            # except User.DoesNotExist:
            #     account = None
            account = authenticate(request, username=username, password=password)
            if account is None:
                messages.error(request, 'Username or password incorrect')
                return HttpResponseRedirect(reverse('login'))
            login(request, account)
            # request.session['username'] = request.POST.get('username')
            return HttpResponseRedirect(reverse('home'))

    context['form'] = form
    return render(request, 'login.html', context)


def home_view(request):
    context = {}
    # username = request.session.get('username')
    # if username is None:
    #     return HttpResponseRedirect(reverse('login'))
    # user = User.objects.get(username=username)
    # context['user'] = user
    return render(request, 'home.html', context)


class MyLogoutView(views.LogoutView):
    template_name = 'login.html'
