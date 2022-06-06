from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')

    context = {
        'form_user': form
    }

    return render(request, "auth_/register.html", context)


def user_logout(request):
    messages.success(request, "You've been logged out successfully")
    logout(request)
    return redirect('list')

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Log in Successfull")
            login(request, user)
            return redirect('list')
    return render(request, 'auth_/user_login.html', {'form' : form})           