# Generated by Django 4.0.4 on 2022-06-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_rename_active_commentmodel_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
