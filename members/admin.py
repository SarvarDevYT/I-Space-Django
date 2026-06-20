from django.contrib import admin
from .models import Category, Product, UserProfile, CartItem, Favorite

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(CartItem)
admin.site.register(Favorite)
