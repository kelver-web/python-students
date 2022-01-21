from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here


class PuclishedManager(models.Manager):
    def get_queryset(self):
        return super(PuclishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = RichTextUploadingField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    description = models.TextField()
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()     # O gerenciador padrão
    published = PuclishedManager() # Meu gerenciador personalizado.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
