# Generated by Django 4.2.10 on 2024-03-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbhood_watch', '0011_remove_user_username_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
