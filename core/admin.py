from django.contrib import admin
from .models import (
    Item, OrderItem, 
    Order, Payment,
    Coupon, BGImages, Refund, Address)

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = 'Update refund order to granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'ordered', 'being_delivered',
        'recieved', 'refund_requested', 'refund_granted',
        'shipping_address', 'billing_address', 'payment', 'coupon']
    
    list_display_links = [
        'user', 'shipping_address', 'billing_address',
        'payment', 'coupon'
    ]
    list_filter = [
        'ordered', 'being_delivered',
        'recieved', 'refund_requested', 'refund_granted'
    ]
    search_fields = [
        'user__username', 'ref_code'
    ]
    actions = [make_refund_accepted]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'street_address', 'apartment_address',
        'country', 'zip_code', 'address_type', 'default'
    ]
    list_filter = [
        'address_type', 'default', 'country'
    ]
    search_fields = [
        'user', 'street_address', 'apartment_address'
    ]

admin.site.register(BGImages)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
