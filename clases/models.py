from django.db import models


class clases(models.Model):
    clases = models.CharField(verbose_name='буква класса', max_length=250)
    number = models.IntegerField(verbose_name='номер класса', default=1)
    teacher = models.CharField(verbose_name='классная руководительница', max_length=255)

    def __str__(self):
        return self.clases

    class Meta:
        verbose_name_plural = 'класс'

#
