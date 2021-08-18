from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Todo, Category
from .forms import TodoForm, ShowForm


def add_todo(request):
    if request.method == 'GET':
    	return render(request, 'add_todo.html', {'todo_list':TodoForm()})   
    elif request.method == 'POST':
        form = TodoForm(request.POST)

       	if form.is_valid():
       		title = form.cleaned_data['title']
       		has_been_done = form.cleaned_data["has_been_done"]
       		date_creation = form.cleaned_data['date_creation']
       		date_completion = form.cleaned_data['date_completion']
       		deadline_date = form.cleaned_data['deadline_date']
       		details = form.cleaned_data["details"]
       		td = Todo(title=title, details=details,has_been_done=has_been_done,date_creation=date_creation,date_completion=date_completion, deadline_date=deadline_date)
       		td.save()
       		
       		return redirect('add_todo')
    else:
       	return render(request, 'add_todo.html', {'todo_list':TodoForm()})
           

def display_todos(request):
	all_todo =Todo.objects.all()
	context = {'todo':all_todo}
	return render(request, 'home.html', context)



