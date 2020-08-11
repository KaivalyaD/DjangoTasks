from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view', views.view_data, name='view'),
]
