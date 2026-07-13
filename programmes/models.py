from django.db import models


class Programme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='programmes/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
