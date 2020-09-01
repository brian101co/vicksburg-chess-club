from django.db import models
from django.urls import reverse

class Tournament(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    start_date = models.DateTimeField()
    ending_date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=200)
    prize = models.CharField(max_length=100, blank=True)
    tournament_format = models.CharField(max_length=100)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    directions = models.TextField()
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tournament_detail', kwargs={
            'slug': self.slug
        })

    
