from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Drug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
