"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import loginPage, registerPage, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from .views import homePageView, aboutPageView, contactPageView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('login/', loginPage, name='login'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', include('carts.urls', namespace='carts')),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('register/', registerPage, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










