# Generated by Django 3.2.7 on 2021-09-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название урока')),
                ('teacher', models.CharField(max_length=255, verbose_name='учитель')),
            ],
            options={
                'verbose_name_plural': 'урок',
            },
        ),
    ]