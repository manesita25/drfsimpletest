# Generated by Django 5.1.3 on 2024-12-01 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyects', '0002_rename_tittle_proyect_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyect',
            old_name='descriptions',
            new_name='description',
        ),
    ]
