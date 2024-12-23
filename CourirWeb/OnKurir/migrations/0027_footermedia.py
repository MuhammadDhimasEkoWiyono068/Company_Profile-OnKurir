# Generated by Django 5.1.1 on 2024-11-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0026_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(choices=[('bi bi-facebook', 'FaceBook'), ('bi bi-youtube', 'YouTube'), ('bi bi-instagram', 'Instagram'), ('bi bi-whatsapp', 'Whatsapp')], max_length=255)),
                ('link', models.URLField(max_length=2000)),
            ],
        ),
    ]
