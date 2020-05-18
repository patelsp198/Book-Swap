# Generated by Django 3.0.2 on 2020-05-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20200331_1857'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
