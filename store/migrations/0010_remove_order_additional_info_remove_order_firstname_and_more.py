# Generated by Django 4.0.3 on 2022-03-26 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='order',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastname',
        ),
    ]
