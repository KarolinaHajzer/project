# coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render

def home(request):
    """
    Moduł dla strony z domowej(zawierającej informacje o stronie), który zwraca jako szablon stronę home.html. 
    """
    context = locals()
    template = "home.html"
    return render(request,template,context)