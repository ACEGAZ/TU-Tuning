from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact/', views.send_contact_email, name="contact"),
    path('contact_success/', views.contact_success, name="contact_success"),
]
