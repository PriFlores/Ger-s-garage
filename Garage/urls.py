"""Garage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from GarageStore import views
## this URL patterns connect the apps to the projects and allow us to use the views in each application as well as Djangp default views
## such as user creation
urlpatterns = [
    path('admin/', admin.site.urls), # default django administrator site
    path('', include('GarageStore.urls')),
    path('Products/', include('Products.urls')),
    path('account/create/', views.signupView, name='signup'),
    path('account/login/', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name= 'signout'),
    path('Orders/', include('Orders.urls')),
    path('shop_cart/', include('shop_cart.urls')),
    path('Bookings/', include('Bookings.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
