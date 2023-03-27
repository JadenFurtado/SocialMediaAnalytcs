from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('search/miserables/',views.miserables),
    path('search/',views.draggable),
    path('clustering/',views.clustering)
]