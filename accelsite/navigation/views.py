from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'navigation/home.html')

def simple_html(request):
    return HttpResponse('<a href="/clearlitmus/last.html">Clear Litmus</a>')