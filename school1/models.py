from django.db import models


class School(models.Model):
    title = models.CharField(verbose_name='Название школы', max_length=255)
    director = models.ForeignKey('director.Director', verbose_name="Директор школы", on_delete=models.CASCADE)
    headteacher = models.ForeignKey('headteacher.Headteacher', verbose_name="Зауч школы", on_delete=models.CASCADE)
    lessons = models.ForeignKey('lessons.Lessons', verbose_name="Уроки", on_delete=models.CASCADE)
    pupils = models.ForeignKey('pupils.Pupils', verbose_name="Ученики", on_delete=models.CASCADE)
    teachers = models.ForeignKey('teachers.Teacher', verbose_name="Учителя", on_delete=models.CASCADE)

    def __str__(self):
        return self.director

    class Meta:
        verbose_name_plural = 'ШКОЛА'
