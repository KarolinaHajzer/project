# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def start(request):
    """
    Moduł dla strony startowej, który zwraca jako szablon stronę index.html. 
    """
    context = locals()
    template = "index.html"
    return render(request,template,context)