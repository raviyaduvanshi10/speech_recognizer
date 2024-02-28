from django.urls import path
from voice_recognizer import views

urlpatterns = [
    path('', views.voice_form, name="voice_form"),
]