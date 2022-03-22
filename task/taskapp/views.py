from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import Registerform


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'name': request.user.username})
    else:
        return HttpResponseRedirect('/login/')

#
# def user_register(request):
#     if request.method == 'POST':
#         fm = Registerform(request.POST)
#         if fm.is_valid():
#             messages.success(request, 'account created')
#             fm.save()
#             return HttpResponseRedirect('/login/')
#     else:
#         fm = Registerform()
#     return render(request, 'register.html', {'form': fm})
#
#
# def user_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             fm = AuthenticationForm(request=request, data=request.POST)
#             if fm.is_valid():
#                 username = fm.cleaned_data['username']
#                 password = fm.cleaned_data['password']
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'login user  !!!!!')
#                     return HttpResponseRedirect('/index/')
#
#         else:
#             fm = AuthenticationForm()
#         return render(request, 'login.html', {'form': fm})
#     else:
#         return HttpResponseRedirect('/index/')


def setsession(request):
    request.session['fname'] = 'Raj'
    request.session['lname'] = 'kanani'
    request.session.set_expiry(500)
    return render(request, 'setsession.html')



# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/login/')


def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=uname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')



def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('/index/')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def user_logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')