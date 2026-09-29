# from django.db import models

# # Create your models here.

# added - 09292026
from django.conf import settings
from django.db import models


class RoleProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or str(self.user)


class Admin(RoleProfile):
    phone_field = "admin_phone"

    admin_id = models.AutoField(primary_key=True)
    admin_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "admin"


class HeadPharmacist(RoleProfile):
    phone_field = "head_pharmacist_phone"

    head_pharmacist_id = models.AutoField(primary_key=True)
    license_number = models.CharField(max_length=100, blank=True)
    head_pharmacist_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "head_pharmacist"


class Pharmacist(RoleProfile):
    phone_field = "pharmacist_phone"

    pharmacist_id = models.AutoField(primary_key=True)
    license_number = models.CharField(max_length=100, blank=True)
    pharmacist_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = "pharmacist"

# # added - 09152026
# from django.contrib.auth.models import User
# from django.db import models


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=150, blank=True)
#     bio = models.TextField(blank=True)

#     def __str__(self):
#         return self.user.username