from django.db import models
from datetime import datetime
# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100, blank=True)
    body=models.TextField(blank=True)
    created_at=models.DateField(default=datetime.now, blank=True)