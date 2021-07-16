# Generated by Django 3.2.5 on 2021-07-16 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
