# Generated by Django 4.0.4 on 2022-06-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
