from django.contrib import admin

from backend.models import CategoryDB, ProductDB

# Register your models here.
admin.site.register(CategoryDB)
admin.site.register(ProductDB)