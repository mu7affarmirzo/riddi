# Generated by Django 2.2.2 on 2020-11-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt_designer', '0006_auto_20201111_1714'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollarType',
        ),
        migrations.AddField(
            model_name='collar',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]