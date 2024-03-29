# Generated by Django 4.1.7 on 2023-03-19 20:47

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('phone_no', models.CharField(max_length=50)),
                ('student_id', models.CharField(default='-', max_length=50)),
                ('batch', models.CharField(default='-', max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collage',
            fields=[
                ('collage', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=50, unique=True)),
                ('course_title', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('credit_hour', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='roll',
            fields=[
                ('roll', models.CharField(max_length=80, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.collage')),
            ],
        ),
        migrations.CreateModel(
            name='courseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('material', models.FileField(max_length=255, upload_to=dashboard.models.courseMaterial.p)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='target_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.department'),
        ),
    ]
