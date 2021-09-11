from django.db import models


class Pupils(models.Model):
    name = models.CharField(verbose_name='Ф.И.О.', max_length=100)
    number = models.IntegerField(verbose_name='класс', default=2)
    phone = models.IntegerField(verbose_name='номер родителей', unique=True)
    plase = models.CharField(verbose_name='Место проживание', max_length=100)

    # photo = models.CharField(verbose_name='фото студента', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ученики'
