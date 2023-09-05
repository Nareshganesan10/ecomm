from django.contrib import admin
from bidit.models import CustomUser, OrderModel, ItemModel


admin.site.register(CustomUser)
admin.site.register(OrderModel)
admin.site.register(ItemModel)
