# Generated by Django 5.1.3 on 2024-11-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beranda',
            name='title_2',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
