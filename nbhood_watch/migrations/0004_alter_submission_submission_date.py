# Generated by Django 4.2.10 on 2024-02-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbhood_watch', '0003_alter_submission_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Report Date:'),
        ),
    ]
