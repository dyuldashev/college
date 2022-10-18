from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    science = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
