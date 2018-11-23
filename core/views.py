from django.shortcuts import render

# /site366/core/views.py

from django.http import HttpResponse
def index(request):
   return HttpResponse('Eu altero o conteúdo em views.py')