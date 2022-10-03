from argparse import Namespace
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name= 'index'),
    path('test', views.test, name='test'),
    path('login', views.login_view, name= 'login'),
    path('logout', views.logout_view, name= 'logout'),
    path('subject', views.subject, name='subject'),
    path('addSub', views.addSub, name='addSub'),
    path('removeSub', views.removeSub, name='removeSub')
]