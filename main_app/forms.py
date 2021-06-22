from django import forms
from django.db.models.fields import DateField
from .models import Order

class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm (forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_date', 'item_ordered', 'box_size', 'customer_name', 'customer_email', 'customer_phone')
        widgets = {
            'order_date': DateInput()
        }