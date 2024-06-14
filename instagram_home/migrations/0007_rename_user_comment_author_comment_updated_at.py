# Generated by Django 5.0 on 2024-06-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_home', '0006_comment_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]