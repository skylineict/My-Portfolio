from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:update-post-list")
    


class Post(models.Model):


    STATUS_CHOICES = (                                 
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    snippet = models.CharField(max_length=100, null=True)
    PreviewImage = models.ImageField(upload_to='PostImage')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    #body = models.TextField()
    publish = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField( max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    category = models.CharField(max_length=50, default='uncategorized')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:update-post-list")
    

    