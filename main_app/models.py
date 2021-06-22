from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Order(models.Model):
    order_date = models.DateField('Date Needed')
    item_ordered = models.CharField(
        ('Item Ordered'),
        max_length=100
    )
    box_size = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order_date} | {self.item_ordered}'
