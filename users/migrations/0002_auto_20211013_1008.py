# Generated by Django 3.2.8 on 2021-10-13 07:08

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_buyer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_supplier',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False, help_text='This is for soft delete'),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('BUYER', 'Buyer'), ('SUPPLIER', 'Supplier'), ('ADMIN', 'Admin')], default='ADMIN', max_length=50, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True, verbose_name='email of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
