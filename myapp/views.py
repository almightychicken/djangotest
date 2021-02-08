from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TestModel

# Create your views here.

def index(request):
	return render(request, 'index.html', {'titles': TestModel.objects.all()})