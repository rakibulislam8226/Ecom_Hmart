# Generated by Django 4.0.3 on 2022-03-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_description_alter_product_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
