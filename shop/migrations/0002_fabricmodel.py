# Generated by Django 2.2.12 on 2020-11-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric', models.CharField(db_index=True, max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('index', models.BooleanField()),
            ],
            options={
                'verbose_name': 'fabric',
                'verbose_name_plural': 'fabrics',
                'ordering': ('price',),
            },
        ),
    ]
