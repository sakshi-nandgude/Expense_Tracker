from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Create Expense model
class Expense(models.Model):
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.amount)