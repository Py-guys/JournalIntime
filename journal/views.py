from django.shortcuts import render, HttpResponse
import mimetypes
from django.contrib import messages
import os

# Create your views here.
def index(request):
    message="""<h6>Do you want to install the application : 
    <span><a href="https://github.com/MeSentreprise/JournalIntime/releases/download/1.0/git-bash.exe"><i class='fa fa-windows'></i> Windows</a></span>
	<pan><a href="https://github.com/MeSentreprise/JournalIntime/releases/download/1.0/git-bash.exe">,<i class='fa fa-apple'></i> macOS </a>et </span>
    <span><a href="https://github.com/MeSentreprise/JournalIntime/releases/download/1.0/git-bash.exe"><i class='fa fa-linux'></i>Linux</a></span></h6>
    """
    return render(request,"Journal/index.html",{
        "message": message
    })