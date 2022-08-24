from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'catalog/index.html')

def parser(request):
    return render(request, 'catalog/parser.html')


