# Generated by Django 2.2.4 on 2019-10-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0011_building_an_construire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='clasa_categorie',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='building',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Alege'), (1, 'Acceptat'), (-1, 'Respins')], db_index=True, default=0),
        ),
    ]