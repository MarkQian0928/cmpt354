# Generated by Django 2.0.7 on 2018-07-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_auto_20180726_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='retailID',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
