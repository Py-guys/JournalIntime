from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(request):
    message="<h6>Do you want to install the application : <span><a href='http://fakebsod.com/windows-8-and-10'><i class='fa fa-windows'></i> Windows</a></span><span><a href='http://fakebsod.com/windows-8-and-10'>, <i class='fa fa-apple'></i> macOS et </a></span><span><a  href='http://fakebsod.com/windows-8-and-10'><i class='fa fa-linux'></i>Linux</a></span></h6>"
    return render(request,"Journal\index.html",{
        "message": message
    })