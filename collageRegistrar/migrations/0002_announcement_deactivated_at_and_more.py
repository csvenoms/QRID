# Generated by Django 4.1.7 on 2023-05-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='deactivated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
