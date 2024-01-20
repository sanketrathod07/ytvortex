from django.http import HttpResponse
from django.shortcuts import render


def webpage1(request):
    return render(request, 'home.html')
def webpage2(request):
    return render(request, 'instagram.html')
def webpage3(request):
    return render(request, 'moreServices.html')