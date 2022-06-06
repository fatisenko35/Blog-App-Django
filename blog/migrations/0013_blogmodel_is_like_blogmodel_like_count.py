# Generated by Django 4.0.4 on 2022-06-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_likemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
