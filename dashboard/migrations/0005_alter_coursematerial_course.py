# Generated by Django 4.1.7 on 2023-03-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_coursematerial_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='course',
            field=models.CharField(max_length=255),
        ),
    ]
