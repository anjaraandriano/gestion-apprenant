# Generated by Django 4.2 on 2023-05-06 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('annee_scolaire', 'classe', 'periode', 'matiere')},
        ),
    ]
