from django.shortcuts import render


def index_view(request):
    return render(request, 'main/index.html')


def mentions_view(request):
    return render(request, 'main/mentions.html')
