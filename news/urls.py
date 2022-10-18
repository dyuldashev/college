from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='galley'),
    path('event/', EvevtListView.as_view(), name='event'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('news/', NewsListView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail')
]