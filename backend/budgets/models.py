from django.db import models

# Create your models here.
class Budget(models.Model):
    limit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    month = models.CharField(max_length=20)

    def __str__(self):
        return self.month