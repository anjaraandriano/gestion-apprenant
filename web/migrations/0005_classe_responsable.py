# Generated by Django 4.2.1 on 2023-05-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_responsable_alter_etudiant_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='responsable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.responsable'),
            preserve_default=False,
        ),
    ]
