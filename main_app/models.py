from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import random


# TUPLE of tuples:
BOX =(
    ('4', '4-pack'),
    ('6', '6-pack'),
    ('12', '12-pack')
)

ORDER=(
    ('Blu', 'Blueberry Muffin'),
    ('Ban', 'Banana Nut Muffin'),
    ('Cra', 'Cranberry Orange Muffin')
)

STATUS=(
    ('pu', 'picked up'),
    ('re', 'ready for pickup'),
    ('sc', 'scheduled'),
    ('ip', 'in progress')

)

# # Create your models here.
class Order(models.Model):
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.customer_name()}'


#Order Tracker Model:------------
class OrderTracker(models.Model):
    status = models.CharField(
        ('status'),
        max_length=2, 
        choices = STATUS, 
        default=STATUS[0][0])
    order_number = models.CharField(
        ('order number'),
        max_length=100),
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.status}'

class Box(models.Model):
    date = models.DateField('Date Needed By')
    box = models.CharField(
        ('box'),
        max_length=2,
        choices=BOX,
        default=BOX[0][0]
    )
    item_ordered = models.CharField(
        ('Choose Your Muffin!'),
        max_length=3,
        choices=ORDER,
        default=ORDER[0][0]

        )
    order_tracker = models.ManyToManyField
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.get_box_display()}|{self.get_item_ordered_display}'