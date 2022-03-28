# Generated by Django 4.0.3 on 2022-03-25 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=60)),
                ('additional_info', models.TextField()),
                ('amount', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Product_images/orders')),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]