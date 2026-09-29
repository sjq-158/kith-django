# from django.db import models

# # Create your models here.

# added - 09292026
from django.conf import settings
from django.db import models


class UserSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user}"

# added - 09152026
# from django.contrib.auth.models import User
# from django.db import models


# class UserSettings(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dark_mode = models.BooleanField(default=False)
#     email_notifications = models.BooleanField(default=True)

#     def __str__(self):
#         return f"Settings for {self.user.username}"