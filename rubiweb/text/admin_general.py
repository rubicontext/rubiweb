#from .models import Track, Artist, Transition, CurrentlyPlaying, TransitionType
#from django.http import HttpResponse

#from django.http import HttpResponseRedirect
from django.shortcuts import render
import psycopg2 as psycopg

def admin_general(request):
	return render(request, 'text/admin_general.html', {'currentTask': None})

def admin_scrap_auto(request):
	return render(request, 'text/shiny_iframe.html', {'currentTask': 'Task Scrap TODO'})