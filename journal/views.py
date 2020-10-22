from django.shortcuts import render
from django.contrib import messages
import os
# Create your views here.
def index(request):
    message="""<h6>Do you want to install the application : 
    <span><a href><i class='fa fa-windows'></i> Windows</a></span>
    <span><a href=''>, <i class='fa fa-apple'></i> macOS </a>et </span>
    <span><a  href=''><i class='fa fa-linux'></i>Linux</a></span></h6>
    """
    return render(request,"Journal\index.html",{
        "message": message
    })