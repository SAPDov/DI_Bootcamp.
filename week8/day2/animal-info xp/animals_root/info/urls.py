
from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('family/<int:id>', views.family, name='family'),
    path('animal/<int:id>', views.animal, name='animal'),
    path('all/', views.all_animals, name ='all'),
    ]
    # path('page', views.page),
    # ,


# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route‏