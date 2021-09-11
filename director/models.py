from django.db import models


class Director(models.Model):
    name = models.CharField(verbose_name='Ф.И.О.', max_length=255)
    phone = models.CharField(verbose_name='номер', max_length=100)
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'директор'
