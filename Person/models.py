from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
def VerifCin(value):
    if len(value)!=8:
        raise ValidationError("cin must have 8 characters!")
def verifEmail(value):
    if str(value).endswith('@esprit.tn'):
        raise ValidationError(f"you email{value} must end with @esprit.tn")
class Person(AbstractUser):
    cin=models.CharField(primary_key=True,max_length=8,validators=[VerifCin])
    email=models.EmailField("Courrier",max_length=50,unique=True,validators=[verifEmail])
    username=models.CharField(max_length=50)