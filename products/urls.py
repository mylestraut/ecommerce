
from django.urls import path

from .views import (
    ProductListView, 
    #product_list_view,
    ProductDetailSlugView, 
    #ProductDetailView, 
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView
    )
app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>', ProductDetailSlugView.as_view(), name='detail'),
]

