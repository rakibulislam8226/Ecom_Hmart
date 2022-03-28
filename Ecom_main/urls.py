from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name='home' ),
    path('search/', search,name='search' ),
    path('contact-with-us/', contact,name='contact_with_us' ),

    path('products/', products,name='products' ),
    path('detail-product/<str:id>/', detail_product,name='detail-product' ),
    
    path('store/', include('store.urls')),
    path('authentication/', include('authentication.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
