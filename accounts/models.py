from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="default_pic.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    RECURRENCE = (
                ('Weekly', 'Weekly'),
                ('Monthly', 'Monthly'),
                ('Anually','Anually'),
    )

    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    tipo = models.CharField(max_length=200, null=True)
    recurrence = models.CharField(max_length=200, null=True, choices=RECURRENCE)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Product(models.Model):
    CATEGORY = (
        ('Eng Elétrica', 'Eng Elétrica'),
        ('Eng Mecânica','Eng Mecânica'),
        ('Eng Civil','Eng Civil'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    #employer = models.ForeignKey(Employer, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name        
=======


>>>>>>> 76ef6bd1a50387b6846e6d4fe1a14682d20e8a78
