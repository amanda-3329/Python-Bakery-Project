# Generated by Django 3.2.4 on 2021-06-23 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210623_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='box_size',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]