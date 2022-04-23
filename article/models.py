from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', default=1, on_delete=models.CASCADE, blank=True)
    doc = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    status = models.BooleanField(default=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title