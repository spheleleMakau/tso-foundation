from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
