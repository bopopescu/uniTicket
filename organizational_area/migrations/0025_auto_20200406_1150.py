# Generated by Django 3.0.3 on 2020-04-06 09:50

from django.db import migrations, models
import organizational_area.models
import uni_ticket.validators


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0024_auto_20200330_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalstructure',
            name='banner',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=organizational_area.models._logo_upload, validators=[uni_ticket.validators.validate_file_size, uni_ticket.validators.validate_file_length]),
        ),
    ]
