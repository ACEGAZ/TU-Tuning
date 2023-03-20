from django.db import models


class Contact(models.Model):
    """ for users to send contact info """
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
