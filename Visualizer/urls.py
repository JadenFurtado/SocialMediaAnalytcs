from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('miserables/',views.miserables),
    path('search',views.draggable)
]