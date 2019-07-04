# Generated by Django 2.0.7 on 2018-07-26 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoes', '0003_auto_20180726_0555'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('CartID', models.AutoField(primary_key=True, serialize=False)),
                ('data_added', models.DateField(auto_now_add=True)),
                ('CustID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['data_added'],
            },
        ),
        migrations.CreateModel(
            name='cartItems',
            fields=[
                ('ItemID', models.AutoField(primary_key=True, serialize=False)),
                ('quanity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('CartID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('ShoeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.Shoes')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
    ]