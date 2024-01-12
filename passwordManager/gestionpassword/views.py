from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def login_view(request):
    #logic de connexion
    return render(request, 'gestionpassword/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'gestionpassword/signup.html', {'form': form})


@login_required
def home_view(request):
    #logic home
    return render(request, 'gestionpassword/home.html')


def add_password_view(request):
    #logic add password
    return render(request, 'gestionpassword/add_password.html')


def view_all_passwords_view(request):
    #logic view all
    return render(request, 'gestionpassword/view_all.html')