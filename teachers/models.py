from django.db import models


class Teacher(models.Model):
    name = models.CharField(verbose_name='Ф.И.О.', max_length=100)
    plase = models.CharField(verbose_name='Место проживание', max_length=100)
    phone = models.IntegerField(verbose_name='номер телефона', unique=True)
    image = models.ImageField(upload_to='image', blank=True)

    # photo = models.CharField(verbose_name='фото учителя', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Учителя'
