from django.urls import path
from . import views

urlpatterns = [
        path('createPerson', views.createPerson),
        path('createList', views.createList),
        path('<int:id>', views.index),
        path('', views.home)
]
