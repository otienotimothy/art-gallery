from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_page(request):
    form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

def login_page(request):
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