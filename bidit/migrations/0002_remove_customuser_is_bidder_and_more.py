# Generated by Django 4.2.5 on 2023-09-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_bidder',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='wallet_balance',
        ),
    ]