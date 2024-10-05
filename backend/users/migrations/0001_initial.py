# Generated by Django 5.1.1 on 2024-10-05 03:38

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='변경일')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='삭제일')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='이름')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='이메일')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images', verbose_name='프로필 이미지')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('permission', models.CharField(default='user', max_length=50, verbose_name='권한')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='직책')),
                ('role', models.CharField(blank=True, max_length=50, null=True, verbose_name='역할')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-created_at'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='변경일')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='삭제일')),
                ('name', models.CharField(max_length=50, verbose_name='팀명')),
                ('team_image', models.ImageField(blank=True, null=True, upload_to='team_images', verbose_name='팀 이미지')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL, verbose_name='팀장')),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='팀원')),
            ],
            options={
                'db_table': 'teams',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.team', verbose_name='팀'),
        ),
    ]