# Generated by Django 3.1.4 on 2020-12-16 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20201215_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='credit_card_partial',
        ),
    ]
