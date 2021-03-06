# Generated by Django 3.0.2 on 2020-03-31 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20200306_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='example@example.com')),
                ('is_staff', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
