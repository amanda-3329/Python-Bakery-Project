# Generated by Django 3.2.4 on 2021-06-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210624_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertracker',
            name='order_number',
            field=models.CharField(default=1, max_length=100, verbose_name='order number'),
            preserve_default=False,
        ),
    ]
