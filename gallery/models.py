from django.db import models


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Sports', 'Sports'),
        ('Community', 'Community'),
        ('Events', 'Events'),
        ('Volunteers', 'Volunteers'),
        ('Children', 'Children'),
    ]
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
