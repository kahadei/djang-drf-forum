# Generated by Django 5.0.6 on 2024-05-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
