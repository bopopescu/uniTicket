# Generated by Django 2.1.7 on 2019-03-05 09:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizationalstructure',
            old_name='type',
            new_name='structure_type',
        ),
        migrations.AlterField(
            model_name='organizationalstructure',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=12000, null=True),
        ),
    ]
