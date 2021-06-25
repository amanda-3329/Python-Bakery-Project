# Generated by Django 3.2.4 on 2021-06-25 22:52

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20210625_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Phone', max_length=31),
        ),
    ]