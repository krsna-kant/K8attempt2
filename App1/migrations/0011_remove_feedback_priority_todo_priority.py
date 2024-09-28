# Generated by Django 4.1.6 on 2023-10-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_feedback_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='priority',
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium', max_length=10, null=True),
        ),
    ]
