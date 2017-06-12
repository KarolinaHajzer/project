from django.http import HttpResponse
from django.template import loader

def home(request):
    context = locals()
    template = "home.html"
    return render(request,template,context)