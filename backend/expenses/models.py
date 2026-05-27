from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Category(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    name = models.CharField(
        max_length=100,
    )

    color = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

# Create Expense model
class Expense(models.Model):

    TYPE_CHOICES = [
        ("expense", "Expense"),
        ("income", "Income"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="expenses",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="expenses",
    )

    description = models.TextField()

    expense_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    def __str__(self):
        return (
            f"{self.amount}"
        )