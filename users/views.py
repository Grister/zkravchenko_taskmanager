from django.shortcuts import render
from django.http import HttpResponse


def sign_up_view(request):
    return HttpResponse("Sign Up page")


def sing_in_view(request):
    return HttpResponse("Sign In page")


def logout_view(request):
    return HttpResponse("Logout page")
