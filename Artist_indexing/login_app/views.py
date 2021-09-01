from django.shortcuts import render
from login_app.forms import UserForm, UserInfoForm

from login_app.models import UserInfo
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user

            user_info.save()

            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()
    dict = {'user_form':user_form,'user_info_form':user_info_form,'registered':registered}
    return render(request,'login_app/register.html', context=dict)

def login_page(request):
    dict = {}
    return render(request, 'login_app/login.html', context=dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('adding:index'))
            else:
                return HttpResponse("Account is not Activate!!")
        else:
            return HttpResponse("Login Details are Wrong!!")
    else:
        return HttpResponseRedirect(reverse('login_app:login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('adding:index'))
