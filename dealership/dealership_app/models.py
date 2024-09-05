from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SERVICE = (
    ('SM', 'Standard Maintenance'),
    ('WA', 'Wash'),
    ('BA', 'Battery'),
    ('AC', 'Air Conditioning'),
    ('WW', 'Windshield Wieprs'),
    ('TP', 'Tire Pressure'),
    ('FS', 'Full Service'),
    ('AL', 'Wheel Alignment'),
    ('BI', 'Brake Service'),
    ('TR', 'Tire Rotation'),
    ('OC', 'Oil Change'),
    ('CC', 'Coolant Service'),
    ('SS', 'Suspension Service'),
    ('PS', 'Power Steering'),
    ('TS', 'Transmission Service'),
    ('ES', 'Engine Service'),
    
)
class Mod(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('mod-detail', kwargs={'pk':self.id})
    class Meta:
        ordering = ['name']
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
    trans = models.CharField('Transmission', max_length=1, choices=TRANS_TYPES)
    epa = models.IntegerField('MPG')
    drivetrain = models.CharField(max_length=1, choices=DRIVETRAIN)
    engine = models.CharField(max_length=250)
    intColor = models.CharField('Interior Color', max_length=25)
    extColor = models.CharField('Exterior Color', max_length=25)
    vin = models.CharField('VIN', max_length=25)
    description = models.TextField()

    mods = models.ManyToManyField(Mod)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.vin
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})

class Service(models.Model):
    date = models.DateField('Service date')
    sType = models.CharField('Service Type', max_length=2, choices=SERVICE, default=SERVICE[0][0])

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_sType_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


