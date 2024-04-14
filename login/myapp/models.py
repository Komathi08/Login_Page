from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    confirm_address = models.TextField()
    state_choices = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        # Add all states in India
    ]
    state = models.CharField(max_length=2, choices=state_choices)
    languages_choices = [
        ('Tamil', 'Tamil'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Telugu', 'Telugu'),
        ('Kannada', 'Kannada'),
    ]
    languages = models.CharField(max_length=10, choices=languages_choices)
