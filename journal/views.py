from django.shortcuts import render, HttpResponse
import mimetypes
from django.contrib import messages
import os
# Create your views here.
def index(request):
    message="""<h6>Do you want to install the application : 
    <span><a href><i class='fa fa-windows'></i> Windows</a></span>
    <span><a href='Downloads\Haha.txt' download="Hamimetypes
    ha.txt">, <i class='fa fa-apple'></i> macOS </a>et </span>
    <span><a  href='/Haha.txt'><i class='fa fa-linux'></i>Linux</a></span></h6>
    """
    return render(request,"Journal\index.html",{
        "message": message
    })
def download_file(request):
    # fill these variables with real values
    fl_path = 'Downloads'
    filename = 'Haha.txt'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response