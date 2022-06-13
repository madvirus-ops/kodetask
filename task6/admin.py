from django.contrib import admin

# Register your models here.
from .models import People, Address, Doctor, Product, Bio, Hotel_Data

admin.site.register(People)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Product)
admin.site.register(Bio)
admin.site.register(Hotel_Data)
