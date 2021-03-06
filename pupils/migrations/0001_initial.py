# Generated by Django 3.2.7 on 2021-09-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ф.И.О.')),
                ('number', models.IntegerField(default=2, verbose_name='класс')),
                ('phone', models.IntegerField(unique=True, verbose_name='номер родителей')),
                ('plase', models.CharField(max_length=100, verbose_name='Место проживание')),
            ],
            options={
                'verbose_name_plural': 'ученики',
            },
        ),
    ]
