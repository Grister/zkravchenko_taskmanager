from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from users.forms import UserRegistrationForm, UserLoginForm


@require_http_methods(["GET", "POST"])
def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('tasks:index')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:sign_in')
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


@require_http_methods(["GET", "POST"])
def sign_in_view(request):
    if request.user.is_authenticated:
        return redirect('tasks:index')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:index')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("users:sign_in")
