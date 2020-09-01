from django.db import models
from django.urls import reverse
from django_quill.fields import QuillField
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = QuillField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='news')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={
            'slug': self.slug
        })

