from django.contrib import admin

from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = Product