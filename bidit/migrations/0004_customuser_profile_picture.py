# Generated by Django 4.2.5 on 2023-09-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidit', '0003_customuser_is_bidder_customuser_wallet_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]