from django.db import models

class SpamNumber(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    spam_count = models.IntegerField(default=0)
