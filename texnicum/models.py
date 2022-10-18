from django.db import models
from django.utils.translation import gettext as _


class DepartmentModels(models.Model):
    title = models.CharField(max_length=555, verbose_name=_('title'))
    short_content = models.TextField(null=True, blank=True, verbose_name=_('short_content'))
    content = models.TextField(null=True, blank=True, verbose_name=_('content'))
    images = models.ImageField(upload_to='department', verbose_name=_('images'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')


class StaffModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    position = models.CharField(max_length=50, verbose_name=_('position'))
    images = models.ImageField(upload_to='staff', verbose_name=_('images'))
    biography = models.TextField(null=True, blank=True, verbose_name=_('biography'))
    short_biography = models.TextField(null=True, blank=True, verbose_name=_('short_biography'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('staff')
        verbose_name_plural = _('staff')


class DocumentsofAdmissionsModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    documents = models.TextField(null=True, blank=True, verbose_name=_('documents'))
    short_document = models.TextField(null=True, blank=True, verbose_name=_('short_document'))
    images = models.ImageField(upload_to='documents', verbose_name=_('images'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')


class VacancyModel(models.Model):
    positions = models.CharField(max_length=150, verbose_name=_('positions'))
    requirement = models.TextField(null=True, blank=True, verbose_name=_('requirement'))
    images = models.ImageField(upload_to='vacancy', verbose_name=_('images'))

    def __str__(self):
        return self.positions

    class Meta:
        verbose_name = _('vacancy')
        verbose_name_plural = _('vacancies')


class BannerModel(models.Model):
    images = models.ImageField(upload_to='banner', verbose_name=_('images'))
    title = models.CharField(max_length=555, verbose_name=_('title'))
    descriptions = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')
