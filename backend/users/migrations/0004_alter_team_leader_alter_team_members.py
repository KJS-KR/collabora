# Generated by Django 5.1.1 on 2024-10-23 11:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL, verbose_name='팀장'),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='팀원'),
        ),
    ]