from django.contrib import admin

from app.models import Product,Category



class ProductAdmin(admin.ModelAdmin):
   list_display=('name','created_at','updated_at')  # chnowa affichi



# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)  #ajouter table product bil crud fil partie admin
  #ajouter table product bil crud fil partie admin
