from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from .models import filesupload



def loginuser(request):
    if request.method=="GET":
        return render(request,'app/loginuser.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'app/loginuser.html',{'form':AuthenticationForm(), 'error':'Username and password do not match'})
        else:
            login(request,user)
            return redirect('fileupload')


def signupuser(request):
    if request.method=="GET":
        return render(request,'app/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['username']=="" or request.POST['password1']=="":
            return render(request,'app/signupuser.html',{'error':'Please enter a valid username and password'})
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('fileupload')
            except IntegrityError:
                return render(request,'app/signupuser.html',{'form':UserCreationForm(), 'error':'Username taken! Please choose a new username'})
        else:
            return render(request,'app/signupuser.html',{'form':UserCreationForm(), 'error':'Password Mismatch!'})
        

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('loginuser')
    

def fileupload(request):
    successmessage=""
    error=""
    if request.method=="POST":
        try:
            file=request.FILES["file"]
            document=filesupload.objects.create(file=file)
            document.save()
            successmessage="File uploaded successfully!"
        except MultiValueDictKeyError:
            error="Please upload a file!"
    return render(request,'app/fileupload.html',{'successmessage':successmessage,'error':error})