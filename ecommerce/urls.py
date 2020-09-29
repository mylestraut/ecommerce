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
from .views import homePageView, aboutPageView, contactPageView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('contact/', contactPageView, name='contact'),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    # path('products/', ProductListView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    # path('products-fbv/', product_list_view),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('products/<slug:slug>', ProductDetailSlugView.as_view()),
    # path('products-fbv/<int:pk>/', product_detail_view),
    path('login/', loginPage, name='login'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cart/', include('carts.urls', namespace='carts')),
    path('register/', registerPage, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










