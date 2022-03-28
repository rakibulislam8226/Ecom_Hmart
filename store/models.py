from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=300)
    message=models.TextField()
    def __str__(self):
        return self.email


class Categories(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Color(models.Model):
    name=models.CharField(max_length=300)
    code=models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Filter_price(models.Model):
    FIlTER_PRICE=(
        ('1000 TO 10000','1000 TO 10000'),
        ('10000 TO 20000','10000 TO 20000'),
        ('20000 TO 30000','20000 TO 30000'),
        ('30000 TO 40000','30000 TO 40000'),
        ('40000 TO 50000','40000 TO 50000'),
    )
    price=models.CharField(max_length=30,choices=FIlTER_PRICE,)
    def __str__(self):
        return self.price



class Product(models.Model):
    CONDITION=(
        ('New','New'),
        ('Old','Old'),
    )
    STOCK=(
        ('IN STOCK','IN STOCK'),
        ('OUT OF STOCK','OUT OF STOCK'),
    )
    STATUS=(
        ('Publish','Publish'),
        ('Draft','Draft'),
    )
    unique_id=models.CharField(unique=True,max_length=30,blank=True,null=True)
    image=models.ImageField(upload_to='media/Product_images/images')
    name=models.CharField(max_length=300)
    price=models.IntegerField()
    condition=models.CharField(max_length=300, choices=CONDITION)
    information=RichTextField(null=True)
    description=RichTextField(null=True)
    stoke=models.CharField(max_length=300, choices=STOCK)
    status=models.CharField(max_length=300, choices=STATUS)
    created_date=models.DateTimeField(auto_now_add=True)

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_price,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
            
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Images(models.Model):
    image=models.ImageField(upload_to='media/Product_images/images')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class Tag(models.Model):
    name=models.CharField(max_length=30)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postcode=models.IntegerField()
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=60)
    amount=models.CharField(max_length=30)
    payment_id=models.CharField(max_length=30,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Product_images/orders')
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    def __str__(self):
        return self.order.user.username






