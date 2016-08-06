from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'clearlitmus/home.html')

def simple_html(request):
    html = "<html><body>This is SMIMPLE HTML from clearlitmus app</body></html>"
    return HttpResponse(html)