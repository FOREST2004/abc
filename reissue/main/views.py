from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .forms import NameForm, CreateBioLower14, CreateBioUpper14
from .models import GetInfor, CCCD
# Create your views here.

def index(response):
    """
    if response.method == "POST":
        if response.POST.get("save"):
            na=response.POST.get('gender')
        
            return render(response, 'temps/t.html', {'text': na})
    """
    return render(response, 'temps/t.html', {})

def tokhaithongtin(response):
    return render(response, 'temps/tokhaithongtin.html', {})
        
def ktrthongtin(response):
    return render(response, 'temps/ktrthongtin.html', {})

def tokhaiduoi14(response):
    if response.method == "POST":

        if response.POST.get("save"):
            
            name=response.POST.get('name')
            birth  = response.POST.get('birthday')
            gender = response.POST.get('gender')
            phonenumber = response.POST.get('sdt')
            location = response.POST.get('location')
            cccd = response.POST.get('cccd')

            return render(response, 'temps/tokhaiduoi14.html', {})
    

    return render(response, 'temps/tokhaiduoi14.html', {})

def tokhaitren14(response):
    return render(response, 'temps/tokhaitren14.html', {})

def laythongtin(response):
    if response.method == "POST":
        if response.POST.get("save"):
            cccd = response.POST.get('cccd')
            if CCCD.objects.filter(cccd=cccd).exists():
                a=CCCD.objects.filter(cccd=cccd).first()
                b=a.getinfor_set.all().first()

                content = {
                    'cccd': b.cccd,
                    'name': b.name,
                    'gender': b.gender,
                    'phonenumber': b.phonenumber,
                    'location': b.location,
                    'guardian': b.guardian,
                    'birth': b.birth,
                }
                return render(response, 'temps/laythongtin2.html', content)
            
            else:
                return render(response, 'temps/laythongtin.html', {'text':'sai'})

        else:
                return render(response, 'temps/laythongtin.html', {'text':'false'})
        
    return render(response, 'temps/laythongtin.html', {})

def tracuu(response):
    return render(response, 'temps/tracuu.html', {})

def thoigiannhanhochieu(response):
    content={
        'queuenumber':'091201',
        'text':'April 12, 2022', 
        'time':'12:02'
    }
    return render(response, 'temps/thoigiannhanhochieu.html', content)