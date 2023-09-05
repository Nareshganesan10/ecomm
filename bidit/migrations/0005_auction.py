# Generated by Django 4.2.5 on 2023-09-04 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bidit', '0004_customuser_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('Auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('auction_start_time', models.DateField()),
                ('auction_end_time', models.DateField()),
                ('winner', models.CharField(max_length=50)),
                ('base_price', models.IntegerField()),
                ('end_price', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidit.itemmodel')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
