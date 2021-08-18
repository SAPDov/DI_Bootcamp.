from django import forms
from .models import Category, Todo


class TodoForm(forms.Form):
	title = forms.CharField(required =True, max_length=30)
	details = forms.CharField(required =True, max_length=500)
	has_been_done = forms.BooleanField()
	date_creation =forms.DateTimeField()
	date_completion = forms.DateField(required= False)
	deadline_date = forms.DateTimeField(required= True)
	category = forms.ModelChoiceField(queryset=Category.objects.all())

class ShowForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    todo = forms.ModelChoiceField(queryset=Todo.objects.all())