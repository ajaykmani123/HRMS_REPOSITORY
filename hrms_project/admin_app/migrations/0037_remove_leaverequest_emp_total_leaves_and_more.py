# Generated by Django 5.0.3 on 2025-01-17 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0036_leaverequest_emp_total_leaves_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='emp_total_leaves',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='emp_used_leaves',
        ),
    ]
