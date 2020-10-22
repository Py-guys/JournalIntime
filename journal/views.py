from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(request):
    message="<h6>Do you want to install the application :<span><a href='http://fakebsod.com/windows-8-and-10'>Windows</a></span></h6>"
    return render(request,"Journal\index.html",{
        "message": message
    })