# Generated by Django 5.0 on 2024-06-11 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_home', '0007_rename_user_comment_author_comment_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
