# Generated by Django 3.1.4 on 2020-12-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]