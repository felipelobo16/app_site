# Generated by Django 3.1.6 on 2021-02-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=30)),
                ('quantidade', models.FloatField(max_length=30)),
                ('valor', models.FloatField(max_length=30)),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
    ]
