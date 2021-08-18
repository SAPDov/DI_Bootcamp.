from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)
	image = models.URLField()

	def __str__(self):
		return f'{self.name}'

class Todo(models.Model):
	title = models.CharField(max_length=80)
	details = models.CharField(max_length=500)
	has_been_done = models.BooleanField(default = False)
	date_creation =models.DateTimeField(auto_now_add=True)
	date_completion = models.DateField(auto_now_add=True)
	deadline_date = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} {self.id}'

