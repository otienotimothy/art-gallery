from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signupUser(request):
    form = RegisterUserForm()
    context = {'form':form}

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'signup.html', context)

def loginUser(request):
    form = LoginUserForm()
    context = {'form': form}

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user_exist = User.objects.get(username=username)
                if user_exist:
                    user = authenticate(
                        request, username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect(index)
                    else: 
                        messages.error(request, 'Invalid username or password')
            except:
                messages.error(request, 'User does not exist, sign-up')
                
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect(loginUser)