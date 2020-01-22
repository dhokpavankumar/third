from django.shortcuts import render
from django.http import HttpResponse

def hell_word(request):
    return HttpResponse("<h1>Hello world this is python world...</h1>")
