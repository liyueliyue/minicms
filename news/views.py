from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("你好，这个是字符串！")
def column_detail(request,column_slug):
    return HttpResponse('column slug:'+column_slug)
def article_detail(request,article_slug):
    return HttpResponse('article slug:'+article_slug)