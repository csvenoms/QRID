# Generated by Django 4.1.7 on 2023-03-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_coursematerial_chapter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='material',
            field=models.FileField(max_length=255, upload_to='Material/'),
        ),
    ]
