# Generated by Django 3.2.10 on 2022-03-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20220311_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='cc_uts',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_cm',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_prov',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_reg',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_rip',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='cod_uts',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='comune',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='comune_a',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='pro_com',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='pro_com_t',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='shape_Area',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='shape_Leng',
        ),
        migrations.AddField(
            model_name='worldborder',
            name='area',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='fips',
            field=models.CharField(max_length=2, null=True, verbose_name='FIPS Code'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='iso2',
            field=models.CharField(max_length=2, null=True, verbose_name='2 Digit ISO'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='iso3',
            field=models.CharField(max_length=3, null=True, verbose_name='3 Digit ISO'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='pop2005',
            field=models.IntegerField(null=True, verbose_name='Population 2005'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='region',
            field=models.IntegerField(null=True, verbose_name='Region Code'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='subregion',
            field=models.IntegerField(null=True, verbose_name='Sub-Region Code'),
        ),
        migrations.AddField(
            model_name='worldborder',
            name='un',
            field=models.IntegerField(null=True, verbose_name='United Nations Code'),
        ),
    ]