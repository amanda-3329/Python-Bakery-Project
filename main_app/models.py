from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



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
    ('sc', 'Scheduled'),
    ('ip', 'In Progress'),
    ('re', 'Ready For Pickup'),
    ('pu', 'Picked up')

)

# # Create your models here.
class Order(models.Model):
    
    customer_name = models.CharField(
        ('Name'),
        max_length=100)
    customer_email = models.CharField(
        ('Email'),
        max_length=100)
    customer_phone = models.CharField(
        ('Phone'),
        max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        ('Order Status'),
        max_length=2, 
        choices = STATUS, 
        default=STATUS[0][0])

    # def __str__(self):
    #     return f'{self.customer_name()}'


#Order Tracker Model:------------
# class OrderTracker(models.Model):
#     status = models.CharField(
#         ('Order Status'),
#         max_length=2, 
#         choices = STATUS, 
#         default=STATUS[0][0])

#     box = models.ManyToManyField
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     def __str__(self):
#         return f'{self.status}'

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