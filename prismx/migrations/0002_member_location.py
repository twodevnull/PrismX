# Generated by Django 3.0.1 on 2020-01-01 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prismx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='location',
            field=models.TextField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
