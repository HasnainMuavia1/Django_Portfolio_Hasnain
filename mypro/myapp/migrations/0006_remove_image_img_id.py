# Generated by Django 5.0.3 on 2024-06-30 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_image_delete_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_id',
        ),
    ]