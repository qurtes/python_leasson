# Generated by Django 5.1.3 on 2025-05-04 12:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comments_options_alter_post_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='fav_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
