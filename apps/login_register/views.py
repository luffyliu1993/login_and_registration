from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request,'login_register/index.html')

def login_check(request):
    login_messages = User.userManager.login(request.session,request.POST['email'],request.POST['password'])
    if login_messages[0]:
        return redirect('/success')
    for message in login_messages[1]['errors']:
        messages.add_message(request,messages.ERROR,message,extra_tags='login')
    return redirect('/')

def register(request):
    register_messages = User.userManager.register_check(request.session,request.POST['fname'],request.POST['lname'],\
            request.POST['email'],request.POST['password'],request.POST['conf_pw'])
    if register_messages[0]:
        return redirect('/success')
    for message in register_messages[1]['errors']:
        messages.add_message(request,messages.ERROR,message,extra_tags='register')
    return redirect('/')

def success(request):
    data = {
        'user':User.userManager.get(id=request.session['id'])
    }
    return render(request,'login_register/success.html',data)
