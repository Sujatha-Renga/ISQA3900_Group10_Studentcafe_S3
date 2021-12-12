from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    path('myorders/<int:username_id>/', views.order_list, name='myorders'),
    path('myorders/<int:username_id>/<int:order_id>', views.order_detail, name='order_detail'),
]
