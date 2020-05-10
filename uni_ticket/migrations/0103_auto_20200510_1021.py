# Generated by Django 3.0.6 on 2020-05-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0102_auto_20200505_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategoryinputlist',
            name='valore',
            field=models.TextField(blank=True, default='', help_text="Viene considerato solo se si sceglie 'Menu a tendina' oppure 'Serie di Opzioni'. (Es: valore1;valore2;valore3...)", max_length=20000, verbose_name='Lista di Valori'),
        ),
    ]
