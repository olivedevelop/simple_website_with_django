from django.urls import path
from . import views

#/products/index
urlpatterns = [
    path('',views.index),
    path('new',views.new)
]
