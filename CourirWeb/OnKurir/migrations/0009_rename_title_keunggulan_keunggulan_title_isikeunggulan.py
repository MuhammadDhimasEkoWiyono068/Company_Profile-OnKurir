# Generated by Django 5.1.3 on 2024-11-08 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0008_rename_banner_beranda_banner_beranda_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keunggulan',
            old_name='title_keunggulan',
            new_name='title_Isikeunggulan',
        ),
    ]
