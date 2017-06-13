# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views hestart(request):re.
def start(request):
    context = locals()
    template = "index.html"
    return render(request,template,context)