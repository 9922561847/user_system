from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from django.http import HttpResponse,HttpResponseRedirect

from .models import UserRegistration
from .forms import UserRegistrationForm,SignUpForm,EditUserProfileForm,EditAdminProfileForm


def sign_up(request):
    """
    using this function user can signup in app
    """
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})


def user_login(request):
    """
    purpose of this function is to check wheather user is authenticated 
    or not, if not it will redirect it to login page.
    only valid user can log into the system
    """
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=username,password=userpass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully !')
                return HttpResponseRedirect('/profile/')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

    else:
        return HttpResponseRedirect('/profile/')


# profile
def user_profile(request):
    """
    function shows userprofile to admin and common user
    1) function checks request is POST or GET
    2) for POST request again it checks logged user is admin or common User
    3) as per the results it shows resp profile.
    4) logged user and admin can edit their resp profiles in this function
    """

    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(request.POST,instance = request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST,instance=request.user)
                users = None # when common user will login it will not through error
            if form.is_valid():
                messages.success(request,'Profile Edited Successfully !')
                form.save()
        else:
            if request.user.is_superuser == True:
                users = User.objects.all()
                form = EditAdminProfileForm(instance=request.user)
            else:
                users = None # when common user will login it will not through error
                form = EditUserProfileForm(instance=request.user)

        return render(request,'profile.html',{'name':request.user,'form':form,'users':users})
    else:
        return HttpResponseRedirect('/login/')



def user_logout(request):
    """
    this function helps user to logout their session
    """
    logout(request)
    return HttpResponseRedirect('/login/')



def user_detail(request,id):
    """
    This funtion takes id as argument so that it will show
    resp. user profile to admin
    """
    if request.user.is_authenticated:
        pk = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance=pk)

        return render(request,'userdetail.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def userregistration(request):
    """
    if userregistration form is valid it saves user information into database
    """
  
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect('/user/')

    else:
        form = UserRegistrationForm()
    return render(request,'user.html',{'form':form})
