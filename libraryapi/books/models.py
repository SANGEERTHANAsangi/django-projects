from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    def __self__(self):
        return self.title
