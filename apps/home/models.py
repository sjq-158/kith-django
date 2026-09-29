# added - 09292026
from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.register.models import Branch, Company


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    requires_prescription = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "medicine"

    def __str__(self):
        return self.medicine_name


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField(default=0)
    reorder_threshold = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "inventory"

    def __str__(self):
        return f"{self.medicine} @ {self.branch}"


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sold_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sale"

    def __str__(self):
        return f"Sale #{self.sale_id}"


class SaleItem(models.Model):
    sale_item_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    quantity_sold = models.IntegerField()
    unit_price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "sale_item"

    def __str__(self):
        return f"{self.quantity_sold} x {self.medicine}"


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    recipient_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification"

    def __str__(self):
        return self.title

# edited - 09292026
# from django.db import models

# # Create your models here.
