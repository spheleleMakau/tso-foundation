from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name
