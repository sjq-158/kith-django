# added - 09292026
from django.contrib import admin

from .models import Branch, Company, User

admin.site.register(Company)
admin.site.register(Branch)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "email", "role", "company", "branch", "is_active")
    readonly_fields = ("password",)

    def has_add_permission(self, request):
        return False  # accounts are created via /register/ or createsuperuser (hashed passwords)


# edited - 09292026
# from django.contrib import admin

# # Register your models here.
