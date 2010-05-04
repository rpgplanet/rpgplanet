from django.db import models

class BetaCandidate(models.Model):
    email = models.CharField(max_length=60, unique=True)
    subscribed = models.DateTimeField(auto_now=True)
