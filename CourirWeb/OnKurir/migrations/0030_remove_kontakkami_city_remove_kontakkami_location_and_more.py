# Generated by Django 5.1.1 on 2024-11-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0029_rename_banner_tentangkami_kontakkami_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontakkami',
            name='city',
        ),
        migrations.RemoveField(
            model_name='kontakkami',
            name='location',
        ),
        migrations.AddField(
            model_name='kontakkami',
            name='embed_gmap',
            field=models.TextField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d997.4213765784025!2d117.15692014227886!3d-0.4675028379033951!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2df67f4979f7e3a9%3A0x7b536c8c2029f57f!2sInformatika%20Universitas%20Mulawarman!5e0!3m2!1sen!2sid!4v1732134348068!5m2!1sen!2sid" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'),
        ),
    ]
