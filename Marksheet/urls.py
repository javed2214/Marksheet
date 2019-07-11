
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('', view.enterMarks),
    path('MarkSheet', view.getMarks, name='MarkSheet'),
]
