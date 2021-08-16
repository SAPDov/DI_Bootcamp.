from django.shortcuts import render
from .models import Animals, Family
import os
import sys


def family(request, id):
	animals = Animals.objects.filter(family__id=id)
	context = {'animals':animals}
	return render(request,'info/family.html',context)


def all_animals (request):
	animals = Animals.objects.all()
	context = {'animals':animals} 
	return render(request,'info/all.html',context)


def animal (request, id):
	animals = Animals.objects.get(id=id)
	context={'animal': animals}
	return render(request,'info/animal.html',context)





	


