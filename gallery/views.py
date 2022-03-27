from unicodedata import name
from django.shortcuts import render
from .forms import RegisterUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_page(request):
    form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

def login_page(request):
    return render(request, 'login.html')