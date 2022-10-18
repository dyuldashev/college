from django.db import models


class FacultiesModel(models.Model):
    faculities = models.CharField(max_length=150)
    information = models.TextField()
    images = models.ImageField(upload_to='faculties')

    def __str__(self):
        return self.faculities

    class Meta:
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'
