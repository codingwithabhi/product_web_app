from django.urls import path,include
from . import views

urlpatterns = [
    path('product-list',views.product_list,name='product-list')
]
