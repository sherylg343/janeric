from django.contrib import admin

from .models import Order, OrderLineItem


# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'shipping_cost', 'order_total', 'grand_total', 'original_cart', 'stripe_pid',)

    fields = ('order_number', 'order_date', 'full_name', 'email', 'phone_number','street_address1', 'street_address2', 'city', 'state', 'zipcode', 'shipping_cost','order_total', 'grand_total', 'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'order_date', 'full_name', 'order_total', 'shipping_cost','grand_total',)

    ordering = ('-order_date', )


admin.site.register(Order, OrderAdmin)
