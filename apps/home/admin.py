# added - 09292026
from django.contrib import admin

from .models import Inventory, Medicine, Notification, Sale, SaleItem

admin.site.register(Medicine)
admin.site.register(Inventory)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Notification)

# edited - 09292026
# from django.contrib import admin

# # Register your models here.
