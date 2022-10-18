from django.db import models
from django.utils.translation import ugettext_lazy as _


class EventModel(models.Model):
    title = models.CharField(max_length=555, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    images = models.ImageField(upload_to='events')
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')


class GalleryModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    images = models.ImageField(upload_to='galleries', verbose_name=_('images'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')


class NewsModel(models.Model):
    title = models.CharField(max_length=555, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    images = models.ImageField(upload_to='news', verbose_name=_('images'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')

