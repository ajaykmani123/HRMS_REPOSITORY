# Generated by Django 5.0.3 on 2025-01-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0016_alter_employees_emp_email_alter_employees_emp_lname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
