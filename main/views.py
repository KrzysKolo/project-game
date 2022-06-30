# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context


def project_info(request):
    template = loader.get_template('main/about.html')
    return HttpResponse(template.render())