from django.shortcuts import render
from .models import Gallery
from django.views.generic import ListView

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
