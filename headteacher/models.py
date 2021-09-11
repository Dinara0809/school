from django.db import models


class Headteacher(models.Model):
    name = models.CharField(verbose_name='Ф.И.О.', max_length=100)
    image = models.ImageField(upload_to='image', blank=True)
    phone = models.IntegerField(verbose_name='номер', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'заучи'
