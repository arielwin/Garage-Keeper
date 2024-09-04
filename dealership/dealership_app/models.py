from django.db import models
from django.urls import reverse

class Car(models.Model):
    TRANS_TYPES = {
        "M": "Manual",
        "A": "Automatic",
        "C": "CVT"
    }
    DRIVETRAIN = {
        '4' : 'Four Wheel Drive',
        'A' : "All Wheel Drive",
        'F' : "Front Wheel Drive",
        'R' : "Rear Wheel Drive"
    }
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    trans = models.CharField(max_length=1, choices=TRANS_TYPES)
    epa = models.IntegerField()
    engine = models.CharField(max_length=250)
    intColor = models.CharField(max_length=25)
    extColor = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
