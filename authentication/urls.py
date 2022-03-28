from django.urls import path
from .views import *


urlpatterns = [
    path('register/',register, name='register' ),
    path('userlogin/',userlogin, name='userlogin' ),
    path('logoutuser/',logoutuser, name='logoutuser' ),
]
