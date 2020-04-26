from django.contrib import admin
from .models import (
    Item, OrderItem, 
    Order, Payment,
    Coupon, BGImages)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']

admin.site.register(BGImages)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Coupon)
