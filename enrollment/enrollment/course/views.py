from urllib import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'course/index.html',)

def test(request):
    return render(request, 'course/test.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'course/login.html',{
                'message' : 'Invalid credentials.'
            })
            
    return render(request, 'course/login.html')