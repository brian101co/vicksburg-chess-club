from django.urls import path
from .views import NewsListing, NewsDetail

urlpatterns = [
    path('', NewsListing.as_view(), name='news_listing'),
    path('<str:slug>/', NewsDetail.as_view(), name='news_detail'),
]