from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Photo, Location
from .forms import RegisterUserForm, LoginUserForm, UploadImageForm

# Create your views here.


@login_required(login_url='login')
def index(request):
    try:
        images = Photo.objects.all()
        locations = Location.objects.all()
        context = {'photos': images, 'locations': locations}
        return render(request, 'index.html', context)
    except:
        messages.error(request, 'An Error occurred while Fetching Images')
    return render(request, 'index.html')


def signupUser(request):
    form = RegisterUserForm()
    context = {'form': form}

    if request.user.is_authenticated:
        return redirect(index)

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print('running')
            user = form.save(commit=False)
            if User.objects.filter(username=user.username.lower()).exists():
                messages.error(
                    request, f'A User with the username, {user.username}, already exists.')
            elif User.objects.filter(email=user.email.lower()).exists():
                messages.error(request,
                               f'A User with the email, {user.email}, already exists.')
            else:
                user.email = user.email.lower()
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect(index)

    return render(request, 'signup.html', context)


def loginUser(request):
    form = LoginUserForm()
    context = {'form': form}

    if request.user.is_authenticated:
        return redirect(index)

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect(loginUser)


@login_required(login_url='login')
def upload(request):
    form = UploadImageForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.added_by_id = request.user.id
            user.save()
            messages.success(request, 'Image Uploaded Successfully')
        else:
            print('form Invalid')
            messages.error(
                request, 'An error occurred while uploading the image')
    return render(request, 'add_image.html', context)
