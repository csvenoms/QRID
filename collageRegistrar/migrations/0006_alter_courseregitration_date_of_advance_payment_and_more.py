# Generated by Django 4.1.7 on 2023-05-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0005_courseregitration_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregitration',
            name='date_of_advance_payment',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courseregitration',
            name='date_of_withdrawal',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courseregitration',
            name='estimated_cost',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
