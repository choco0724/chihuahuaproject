# chihuapp/urls.py
from django.urls import path
from . import views

app_name = 'chihuapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
