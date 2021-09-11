from django.db import models
from django.db import models


class lessons(models.Model):
    title = models.CharField(verbose_name='название урока', max_length=255)
    teacher = models.CharField(verbose_name='учитель', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'урок'
