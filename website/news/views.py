
from __future__ import unicode_literals
from django.shortcuts import render

def news(request):
    context = locals()
    template = "news.html"
    return render(request,template,context)