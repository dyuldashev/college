from django.db import models


class StatisticsModel(models.Model):
    subjects = models.CharField(max_length=555)
    students = models.CharField(max_length=555)
    modern_labs = models.CharField(max_length=555)
    teacher = models.CharField(max_length=555)

    def __str__(self):
        return self.students

    class Meta:
        verbose_name = 'statistics'
        verbose_name_plural = 'statistics'

