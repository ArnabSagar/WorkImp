from django.db import models

class Whitelist(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=120)

    def __str__(self):
        return self.name
