from django.db import models
from datetime import date

# Create your models here.
class ShoppingItem(models.Model):
    LIST_CHOICES = [('erledigungen', 'Erledigungen'), ('besorgungen', 'Besorgungen')]
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    list_type = models.CharField(max_length=20, choices=LIST_CHOICES, default='erledigungen')

    def __str__(self):
        return str(self.id) + ' ' + self.name