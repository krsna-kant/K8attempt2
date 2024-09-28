# Generated by Django 4.1.6 on 2023-10-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_alter_feedback_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='experience',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')], default='Good', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='type',
            field=models.CharField(blank=True, choices=[('Bug', 'Bug'), ('Suggestion', 'Suggestion')], default='Suggestion', max_length=10, null=True),
        ),
    ]
