from django.contrib import admin
from .models import (
    Item, OrderItem, 
    Order, Payment,
    Coupon, BGImages)


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'ordered', 'being_delivered',
        'recieved', 'refund_requested', 'refund_granted',
        'billing_address', 'payment', 'coupon']
    
    list_display_links = [
        'user', 'billing_address',
        'payment', 'coupon'
    ]
    list_filter = [
        'ordered', 'being_delivered',
        'recieved', 'refund_requested', 'refund_granted'
    ]
    search_fields = [
        'user__username', 'ref_code'
    ]

admin.site.register(BGImages)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Coupon)
