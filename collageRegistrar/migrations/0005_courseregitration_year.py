# Generated by Django 4.1.7 on 2023-05-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collageRegistrar', '0004_rename_demand_service_cash_courseregitration_demand_service_cashkind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregitration',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]