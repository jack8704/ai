from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 경로 ( home/views.py)

def home(request):
  #return HttpResponse('<h1>hello django</h1>')
  return render(request,
                'home.html',          # templates 페이지      # 폴더/templates/home.html
                context={'msg': "Django(장고)"})