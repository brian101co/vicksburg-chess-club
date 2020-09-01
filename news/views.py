from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class NewsListing(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'

