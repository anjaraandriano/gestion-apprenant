# Generated by Django 4.2.1 on 2023-06-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_etudiant_lieu_de_naissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenir',
            name='observation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]