from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('Main page')


def about_view(request):
    return HttpResponse('About page')


def detail_view(request, uuid):
    return HttpResponse(f'Task {uuid} detail')


def create_view(request):
    return HttpResponse('Create task')


def update_view(request, uuid):
    return HttpResponse(f'Update task {uuid}')


def delete_view(request, uuid):
    return HttpResponse(f'Delete task {uuid}')
