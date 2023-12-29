from django.db import models

# Create your models here.
class nav(models.Model):
    name=models.CharField(max_length=20)
    des=models.CharField(max_length=500)
    image=models.ImageField(upload_to='nav')
    def __str__(self):
        return self.name
