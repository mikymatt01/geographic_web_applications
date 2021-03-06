# Generated by Django 3.2.10 on 2022-03-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('italy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='italy',
            name='GlobalID',
            field=models.CharField(max_length=38, null=True),
        ),
        migrations.AddField(
            model_name='italy',
            name='SHAPE_Le_1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='italy',
            name='fid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='italy',
            name='comune',
            field=models.CharField(max_length=34, null=True, verbose_name='comune'),
        ),
        migrations.AlterField(
            model_name='italy',
            name='comune_a',
            field=models.CharField(max_length=36, null=True, verbose_name='comune_a'),
        ),
    ]
