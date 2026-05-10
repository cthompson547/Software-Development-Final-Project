from django.db import models

# Create your models here.

class CreateOrder(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        # Ensure price is non-negative
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ${self.price}"