# Generated by Django 3.2 on 2021-04-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210408_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_description',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(to='school.Students'),
        ),
    ]
