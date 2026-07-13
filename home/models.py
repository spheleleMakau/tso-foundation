from django.db import models


class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Hero Slides'

    def __str__(self):
        return self.title
