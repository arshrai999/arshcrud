# Generated by Django 3.0.5 on 2021-04-07 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
                ('Address2', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
                ('Zip', models.IntegerField()),
            ],
        ),
    ]
