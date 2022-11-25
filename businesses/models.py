from django.db import models

class Business (models.Model):
    name = models.CharField(max_length=19, unique=True)
    owner = models.ForeignKey(
        "owners.User",
        on_delete=models.CASCADE,
        blank=False,
        null = False,
        related_name="businesses"
    )
