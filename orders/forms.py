from django import forms
from .models import Order, Product, CustomUser


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        exclude = ('username',)



        # Exclude 'username field here, it will be added with current user name
