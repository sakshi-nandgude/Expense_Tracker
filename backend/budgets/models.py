import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Budget(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="budgets",
    )

    limit_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    warning_threshold = models.IntegerField()

    month = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return (
            f"{self.user} - {self.month}"
        )