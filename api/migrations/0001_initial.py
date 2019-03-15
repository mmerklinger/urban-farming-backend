# Generated by Django 2.0.13 on 2019-03-14 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPointsOxygen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DataPointsPh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DataPointsTemperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemId', models.CharField(max_length=5)),
                ('systemSecret', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='datapointstemperature',
            name='systemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.System'),
        ),
        migrations.AddField(
            model_name='datapointsph',
            name='systemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.System'),
        ),
        migrations.AddField(
            model_name='datapointsoxygen',
            name='systemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.System'),
        ),
    ]
