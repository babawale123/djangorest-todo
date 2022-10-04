from django.db import models
from django.models import user

# Create your models here.

class Purchase(models.Model):
    user = models.ForeignKey(
        user, related_name='purchases', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    litres = models.DecimalField(decimal_places=2, max_digits=10)
    reference = models.CharField(max_length=400)
    exhausted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
