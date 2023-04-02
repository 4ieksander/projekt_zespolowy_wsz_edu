# Generated by Django 3.2.18 on 2023-04-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_organ_players', '0006_player_bitcoins_player_dollars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booster',
            name='name_of_booster',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name_of_equipment',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='medicalstaff',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='medicalstaff',
            name='surname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='organstoragearea',
            name='storage_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='playerattributes',
            name='attribute',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='technicalstaff',
            name='surname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='technicalstaff',
            name='username',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiclestoragearea',
            name='storage_name',
            field=models.CharField(max_length=50),
        ),
    ]
