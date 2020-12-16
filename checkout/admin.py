from django.contrib import admin

from .models import Order, OrderLineItem


# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'shipping_cost', 'order_total', 'grand_total', 'original_cart', 'stripe_pid',)

    fields = (
        'order_number', 'order_date', 'ship_full_name', 'email', 'ship_phone_number','ship_street_address1', 'ship_street_address2', 'ship_city', 'ship_state', 'ship_zipcode', 'shipping_cost','order_total', 'grand_total', 'original_cart', 'stripe_pid', 'bill_full_name', 'bill_phone_number','bill_street_address1', 'bill_street_address2', 'bill_city', 'bill_state', 'bill_zipcode',)

    list_display = ('order_number', 'order_date', 'email', 'order_total', 'shipping_cost','grand_total', 'ship_full_name', 'ship_phone_number','ship_street_address1', 'ship_street_address2', 'ship_city', 'ship_state', 'ship_zipcode', 'bill_full_name', 'bill_phone_number','bill_street_address1', 'bill_street_address2', 'bill_city', 'bill_state', 'bill_zipcode',)

    ordering = ('-order_date', )


admin.site.register(Order, OrderAdmin)
