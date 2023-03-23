from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def home(request):
    """ a view to return the home page"""
    return render(request, "home.html")


def about_us(request):
    """ a view to return the about_us page"""
    return render(request, "about_us.html")


def contact_success(request):
    """ a view to return the contact_success page"""
    return render(request, "contact_success.html")


def send_contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = ('New Inquiry')
            full_name = request.POST.get('full_name', '')
            phone_number = request.POST.get('phone_number', '')
            email = request.POST.get('email', '')
            body = {
                    'full_name': form.cleaned_data['full_name'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'Registration': form.cleaned_data['Registration'],
                    'email': form.cleaned_data['email'],
                    }
            message = "\n".join(body.values())

        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                      ['tutuningperformance@gmail.com'],)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, "contact_success.html")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
