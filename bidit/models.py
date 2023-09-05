from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_bidder = models.BooleanField(null=True)
    wallet_balance = models.IntegerField(null=True)
    profile_picture = models.ImageField(null=True)


class ItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.TextField()
    item_image = models.ImageField(null=True)
    catagory = models.CharField(max_length=50)
    base_price = models.IntegerField()
    owner_count = models.IntegerField()


    def __str__(self):
        return self.item_name
    

class OrderModel(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_id


class Auction(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    Auction_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    auction_start_time = models.DateField(auto_now=False, auto_now_add=False)
    auction_end_time = models.DateField(auto_now=False, auto_now_add=False)
    winner = models.CharField(max_length=50)
    base_price = models.IntegerField()
    end_price = models.IntegerField()

    def __str__(self):
        return self.Auction_id