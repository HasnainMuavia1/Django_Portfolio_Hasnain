# Generated by Django 5.0.3 on 2024-06-30 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extend',
            old_name='desription',
            new_name='description',
        ),
    ]
