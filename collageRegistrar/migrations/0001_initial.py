# Generated by Django 4.1.7 on 2023-04-27 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('announcer', models.CharField(max_length=50)),
                ('announcement', models.ImageField(upload_to='announcements/')),
                ('announcement_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]