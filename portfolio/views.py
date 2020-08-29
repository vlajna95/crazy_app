# from django.shortcuts import render
from django.http import HttpResponse

def index(request, *args, **kwargs):
	return HttpResponse("The app is a WiP, please be patient. 😀")