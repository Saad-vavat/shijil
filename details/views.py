from re import S
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='home')
def info(request):
    context={'sites':Sites.objects.all()}
    return render(request, 'info.html',context)
