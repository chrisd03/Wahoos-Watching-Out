# Generated by Django 4.2.10 on 2024-03-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nbhood_watch", "0012_submission_submission_desc"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="submission_status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("In Progress", "In Progress"),
                    ("Reviewed", "Reviewed"),
                ],
                default="New",
                max_length=20,
            ),
        ),
    ]
