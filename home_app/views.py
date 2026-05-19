from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_page(request):
    return HttpResponse("<h1>Hello from Django inside Docker!</h1>")

def index_new(request):
    return render(request,('home_app/index.html'))
