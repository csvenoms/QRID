# Generated by Django 4.1.7 on 2023-05-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_course_semister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.CharField(default='', max_length=50),
        ),
    ]
