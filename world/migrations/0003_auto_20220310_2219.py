# Generated by Django 3.2.10 on 2022-03-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20220310_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_pro',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='den_cmpro',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='flag_cmpro',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='provincia',
        ),
        migrations.AddField(
            model_name='worldborder',
            name='cod_prov',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='cod_rip',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='cod_uts',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='den_cm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='den_prov',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='den_uts',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='tipo_uts',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='cod_cm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='cod_reg',
            field=models.IntegerField(null=True),
        ),
    ]
