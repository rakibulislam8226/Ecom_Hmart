from django.contrib import admin
from . models import *


# Register your models here.
class ImagesTublerinline(admin.TabularInline):
    model=Images
class TagTublerinline(admin.TabularInline):
    model=Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagTublerinline]

class OrderItemTublerinline(admin.TabularInline):
    model=OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTublerinline]
    list_display=['user','email','paid','payment_id','date']
    search_fields=['user','email','paid','payment_id','date']


admin.site.register(Contact)

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_price)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Product,ProductAdmin)

admin.site.register(OrderItem)
admin.site.register(Order,OrderAdmin)






