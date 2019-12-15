# Generated by Django 3.0 on 2019-12-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=20)),
                ('imagen', models.FilePathField(path='/img')),
            ],
        ),
    ]
