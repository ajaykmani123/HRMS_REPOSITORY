# Generated by Django 5.0.3 on 2025-01-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0038_employees_emp_total_leaves_employees_emp_used_leaves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='leave_type',
            field=models.CharField(choices=[('Floating Leave', 'Floating Leave'), ('Casual Leave', 'Casual Leave')], default='Casual Leave', max_length=20),
        ),
    ]
