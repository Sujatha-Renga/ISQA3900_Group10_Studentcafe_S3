from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SignUpView

app_name = 'cafe'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.menu_list, name='product_list_by_category'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),

]
