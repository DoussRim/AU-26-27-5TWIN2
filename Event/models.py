from django.db import models
from Person.models import Person
from datetime import datetime
# Create your models here.
class Event(models.Model):
    category_list=(
        ('M','Musique'),
        ('C',"Cinema"),
        ('S','Sport'),
    )
    title=models.CharField("Titel",max_length=50)
    description=models.TextField(max_length=50)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    category=models.CharField(choices=category_list)
    state=models.BooleanField(default=False)
    nb_participant=models.IntegerField(default=0)
    evt_date=models.DateTimeField()
    creation_date=models.DateTimeField(auto_now_add=True)
    update_date =models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True
    )
    participant=models.ManyToManyField(
        Person,
        through="Participants"
    )
    class Meta:
        contraints=[
            models.CheckConstraint(check=models.Q(
                evt_date__gt=datetime.now()
            ),
            name="Please check date event")
        ]
class Participants(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=['person','event']