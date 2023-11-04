from django.db import models

class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description", max_length=999)
    price = models.PositiveIntegerField()
    image = models.ImageField()


