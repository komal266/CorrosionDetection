# Generated by Django 3.2.10 on 2022-02-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220212_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictsearches',
            name='og_image',
        ),
        migrations.RemoveField(
            model_name='predictsearches',
            name='rust_image',
        ),
        migrations.RemoveField(
            model_name='predictsingle',
            name='rust_image',
        ),
    ]
