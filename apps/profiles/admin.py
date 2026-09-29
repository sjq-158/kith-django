# from django.contrib import admin

# # Register your models here.

# added - 09292026
from django.contrib import admin

from .models import Admin, HeadPharmacist, Pharmacist

admin.site.register(Admin)
admin.site.register(HeadPharmacist)
admin.site.register(Pharmacist)

# added - 09152026
# from django.contrib import admin
# from .models import Profile

# admin.site.register(Profile)