from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class NewsListView(ListView):
    template_name = 'news.html'
    queryset = NewsModel.objects.order_by('-pk')


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'news_detail.html'


class EvevtListView(ListView):
    template_name = 'event.html'
    queryset = EventModel.objects.order_by('-pk')


class EventDetailView(DetailView):
    model = EventModel
    template_name = 'event_detail.html'


class GalleryListView(ListView):
    model = GalleryModel
    paginate_by = 3
    template_name = 'galleries.html'
