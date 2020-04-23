from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index_view(request):
    return render(request, 'main/index.html')


def mentions_view(request):
    return render(request, 'main/mentions.html')

