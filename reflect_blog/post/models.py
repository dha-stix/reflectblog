from datetime import datetime

from django.db import models
from django.utils.text import slugify


# CATEGORY MODEL
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# AUTHOR MODEL
class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# POST MODEL
class Post(models.Model):
    POST_STATUS = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),)
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.PositiveIntegerField()
    cover_image = models.ImageField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=200)
    short_description = models.CharField(max_length=150, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=POST_STATUS)

    def __str__(self):
        return f"{self.title} was {self.status} on {self.timestamp}"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
