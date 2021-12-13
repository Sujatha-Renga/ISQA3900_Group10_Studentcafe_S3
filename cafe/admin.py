from django.contrib import admin
from .models import Category, Product

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category_image']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'description', 'available_qty', 'created', 'updated', 'category', 'image', 'calories']
    list_filter = ['available', 'available_qty', 'category']
    list_editable = ['price', 'available', 'available_qty', 'description']
    prepopulated_fields = {'slug': ('name',)}


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'cell_phone', 'is_staff' ]


admin.site.register(CustomUser, CustomUserAdmin)
