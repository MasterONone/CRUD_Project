# Generated by Django 5.1.5 on 2025-03-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('DateOfBirth', models.DateField()),
                ('Course', models.CharField(max_length=100)),
                ('EnrollmentDate', models.DateField()),
            ],
        ),
    ]
