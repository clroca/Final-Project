from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from mysite.models import *


def home(request):
	return render(request, 'home.html')
