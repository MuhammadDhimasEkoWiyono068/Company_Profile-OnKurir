# Generated by Django 5.1.1 on 2024-11-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnKurir', '0020_layanan_title_kebijakanketentuan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
