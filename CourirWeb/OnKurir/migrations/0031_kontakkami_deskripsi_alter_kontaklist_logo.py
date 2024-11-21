# Generated by Django 5.1.1 on 2024-11-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0030_remove_kontakkami_city_remove_kontakkami_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakkami',
            name='deskripsi',
            field=models.TextField(default='Apakah Anda memiliki pertanyaan tentang layanan kami? Jangan ragu untuk menghubungi kami'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kontaklist',
            name='logo',
            field=models.CharField(choices=[('bi bi-envelope', 'E-mail'), ('bi bi-telephone', 'Telp'), ('bi bi-geo-alt', 'Alamat')], default='bi bi-envelope', max_length=255, unique=True),
        ),
    ]