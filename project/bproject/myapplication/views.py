from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request,"home.html")
def reference(request):
    return render(request,"reference.html")
def books(request):
    return render(request,"books.html")
def ebooks(request):
    return render(request,"ebooks.html")
def journals(request):
    return render(request,"journals.html")
def about(request):
    return render(request,"about.html")
def doctor(request):
    return render(request,"doctor.html")

