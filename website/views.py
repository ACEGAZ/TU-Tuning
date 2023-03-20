from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def home(request):
    """ a view to return the home page"""
    return render(request, "home.html")


def about_us(request):
    """ a view to return the about_us page"""
    return render(request, "about_us.html")


def contact(request):
    """ a view to return the contact page"""
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, "contact.html", context)
