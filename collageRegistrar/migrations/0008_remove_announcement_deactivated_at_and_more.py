# Generated by Django 4.1.7 on 2023-06-01 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0007_gradecsvs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='is_active',
        ),
    ]
