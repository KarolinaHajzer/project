# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

def news(request):
    """
    Moduł dla strony z informacjami o przecenach, który zwraca jako szablon stronę news.html. 
    """
    context = locals()
    template = "news.html"
    return render(request,template,context)
