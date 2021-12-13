from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    category_image = models.ImageField(upload_to='cafe/static/images/categories_image/', null=True, blank=True)

    #    created_date = models.DateTimeField(default=timezone.now)
    #    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cafe:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category =  models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200)
    available_qty = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cafe/static/images/product_image/', null=True, blank=True)
    calories = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created = timezone.now()
        self.save()

    def updated(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cafe:product_detail',
                       args=[self.id, self.slug])

class CustomUser(AbstractUser):
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')