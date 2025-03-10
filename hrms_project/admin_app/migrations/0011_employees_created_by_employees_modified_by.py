# Generated by Django 5.0.3 on 2025-01-02 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0010_remove_employees_emp_password'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_employees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employees',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_employees', to=settings.AUTH_USER_MODEL),
        ),
    ]
