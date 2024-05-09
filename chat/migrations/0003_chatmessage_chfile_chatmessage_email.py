# Generated by Django 4.1.7 on 2023-05-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessage_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='chfile',
            field=models.FileField(blank=True, null=True, upload_to='chat/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='email',
            field=models.CharField(default='', max_length=250),
        ),
    ]
