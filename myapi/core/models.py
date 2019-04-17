from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField()
    tell = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s-%d" % (self.title, self.pk)

