# Generated by Django 4.1.7 on 2023-05-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0006_alter_courseregitration_date_of_advance_payment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeCSVs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='grades/')),
                ('dept', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
            ],
        ),
    ]
