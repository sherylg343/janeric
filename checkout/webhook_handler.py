from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
                billing_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.defaultship_full_name = shipping_details.name,
                profile.defaultship_street_address1 = shipping_details.address.line1,
                profile.defaultship_street_address2 = shipping_details.address.line2,
                profile.defaultship__city = shipping_details.address.city,
                profile.defaultship_state = shipping_details.address.state,
                profile.defaultship_zipcode = shipping_details.address.postal_code,
                profile.defaultship_phone_number = shipping_details.phone,
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    ship_full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    ship_phone_number__iexact=shipping_details.phone,
                    ship_street_address1__iexact=shipping_details.address.line1,
                    ship_street_address2__iexact=shipping_details.address.line2,
                    ship_city__iexact=shipping_details.address.city,  
                    ship_state__iexact=shipping_details.address.state,
                    ship_zipcode__iexact=shipping_details.address.postal_code,
                    bill_full_name__iexact=billing_details.name,
                    bill_phone_number__iexact=billing_details.phone,
                    bill_street_address1__iexact=billing_details.address.line1,
                    bill_street_address2__iexact=billing_details.address.line2,
                    bill_city__iexact=billing_details.address.city,  
                    bill_state__iexact=billing_details.address.state,
                    bill_zipcode__iexact=billing_details.address.postal_code,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    ship_full_name=shipping_details.name,
                    email=billing_details.email,
                    ship_phone_number=shipping_details.phone,
                    ship_street_address1__iexact=shipping_details.address.line1,
                    ship_street_address2__iexact=shipping_details.address.line2,
                    ship_city__iexact=shipping_details.address.city,  
                    ship_state__iexact=shipping_details.address.state,
                    ship_zipcode__iexact=shipping_details.address.postal_code,
                    bill_full_name__iexact=billing_details.name,
                    bill_phone_number__iexact=billing_details.phone,
                    bill_street_address1__iexact=billing_details.address.line1,
                    bill_street_address2__iexact=billing_details.address.line2,
                    bill_city__iexact=billing_details.address.city,  
                    bill_state__iexact=billing_details.address.state,
                    bill_zipcode__iexact=billing_details.address.postal_code,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for product_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=product_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
