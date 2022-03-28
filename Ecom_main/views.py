
from django.shortcuts import redirect, render
from store.models import *
from django.core.mail import send_mail
def Home(request):
    product=Product.objects.all()
    context={
        'product':product,
    }
    return render(request,'main/index.html',context)


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

                #for email me start#
        data={
        'name':name,
        'email':email,
        'subject':subject,
        'message':message,
        }
        message = ''' 
        {}

        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['name'],message, '',['rakibkhan9065@gmail.com'])
        #for email me end#

        obj=Contact(name=name,email=email,subject=subject,message=message)
        obj.save()
        return redirect('home')

    return render(request,'main/contact.html')


def products(request):
    category=Categories.objects.all()
    filter_price=Filter_price.objects.all()
    color=Color.objects.all()
    brand=Brand.objects.all()

    CATID=request.GET.get('categories')
    FILTER_PRICE=request.GET.get('filter_price')
    COLORID=request.GET.get('color')
    BANID=request.GET.get('brand')

    ATOZID=request.GET.get('AtoZ')
    ZTOAID=request.GET.get('ZtoA')
    PriceLowToHighID=request.GET.get('priceLowToHigh')
    PriceHighToLowID=request.GET.get('priceHighToLow')
    NEWID=request.GET.get('new')
    OLDID=request.GET.get('old')


    if CATID:
        product=Product.objects.filter(categories = CATID)

    elif FILTER_PRICE:
        product=Product.objects.filter(filter_price = FILTER_PRICE)

    elif COLORID:
        product=Product.objects.filter(color = COLORID)

    elif BANID:
        product=Product.objects.filter(brand = BANID)

    elif ATOZID:
        product=Product.objects.all().order_by('name')

    elif ZTOAID:
        product=Product.objects.all().order_by('-name')

    elif PriceLowToHighID:
        product=Product.objects.all().order_by('price')

    elif PriceHighToLowID:
        product=Product.objects.all().order_by('-price')

    elif NEWID:
        product=Product.objects.all().order_by('-created_date')

    elif OLDID:
        product=Product.objects.all().order_by('created_date')

    else:
        product=Product.objects.all()
        
    

    context={
        'product':product,
        'category':category,
        'filter_price':filter_price,
        'color':color,
        'brand':brand,
    }
    return render(request,'main/products.html',context)


def search(request):
    query=request.GET.get('query')
    product=Product.objects.filter(name__icontains = query)

    context={
        'product':product,
    }
    return render(request,'main/search.html',context)


def detail_product(request,id):
    prod=Product.objects.filter(id=id).first()

    context={
        'prod':prod,
    }
    return render(request,'main/product_detail.html',context)





































