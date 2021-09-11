from django.contrib import admin
from director.models import Director
from headteacher.models import Headteacher
from teachers.models import Teacher
from clases.models import clases
from lessons.models import lessons
from pupils.models import Pupils
from .models import School

admin.site.register(School)
admin.site.register(Director)
admin.site.register(Headteacher)
admin.site.register(Teacher)
admin.site.register(clases)
admin.site.register(lessons)
admin.site.register(Pupils)
