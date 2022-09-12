from distutils.util import subst_vars
from genericpath import exists
from re import sub
from subprocess import STARTF_USESTDHANDLES
from urllib import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from course.models import Course, Enrollment
from django.contrib.auth.models import User

# Create your views here.
    
       
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    user_data = User.objects.get(id=request.user.id)
    enrollment = Enrollment.objects.filter(user=user_data)
    print(enrollment)
    return render(request, 'course/index.html', {
        'enrollment' : enrollment
    })
    

def test(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'course/test.html')

def subject(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    subject = Course.objects.all()
    
    return render(request, 'course/subject.html', {
        'subject' : subject,

        
    })

def addSub(request):
    user = User.objects.get(id=request.user.id)
    subject = Course.objects.get(pk = request.POST["action"])
    enroll = Enrollment.objects.create(user=user, courses=subject)
    subject.registered.add(request.user)
    return HttpResponseRedirect(reverse('subject'))

def removeSub(request):
    user = User.objects.get(id=request.user.id)
    subject = Course.objects.get(pk = request.POST["unaction"])
    enroll = Enrollment.objects.get(user=user, courses=subject)
    enroll.delete()
    subject.registered.remove(request.user)
    return HttpResponseRedirect(reverse('subject'))

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

def logout_view(request):
    logout(request)
    return render(request, 'course/login.html', {
        'message' : 'Logged out !'
    })

