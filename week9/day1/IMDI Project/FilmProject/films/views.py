from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Country, Director, Category, Film
from .forms import AddFilmForm, AddDirectorForm
from django.views.generic import View, ListView, CreateView, DeleteView, DetailView, UpdateView
# Create your views here.




def home(request):
	films = Film.objects.all()
	return render(request, 'homepage.html', {'films':films})


class FilmListView(ListView):
	model = Film

class DirectorListView(ListView):
	model = Director


class AddFilm(CreateView):
	form_class = AddFilmForm
	template_name = 'film/addFilm.html'
	success_url = reverse_lazy('home')

class AddDirector(CreateView):
	form_class =  AddDirectorForm
	template_name = 'director/addDirector.html'
	success_url = reverse_lazy('home')



