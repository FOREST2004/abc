from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm
from .models import GetInforLowwer14, GetInforLowwer14
# Create your views here.

def index(response):
    return render(response, 'temps/t.html', {})

def tokhaithongtin(response):
    return render(response, 'temps/tokhaithongtin.html', {})
        
def ktrathongtin(response):
    return render(response, 'temps/ktrathongtin.html', {})

def tokhaiduoi14(response):
    name=response.POST.get['name']
    birth=response.POST.get['birthday']
    return render(response, 'temps/tokhaiduoi14.html', {})

def tokhaitren14(response):
    return render(response, 'temps/tokhaitren14.html', {})