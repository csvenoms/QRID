# Generated by Django 4.1.7 on 2023-05-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='messages/files/'),
        ),
    ]
