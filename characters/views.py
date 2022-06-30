from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context


def characters_list(request):
    template = loader.get_template('character/characters_list.html')
    return HttpResponse(template.render())