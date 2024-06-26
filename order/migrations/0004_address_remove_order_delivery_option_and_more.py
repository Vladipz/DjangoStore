# Generated by Django 4.2.13 on 2024-05-15 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_deliveryprovider_alter_order_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_option',
        ),
        migrations.DeleteModel(
            name='DeliveryProvider',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.address'),
        ),
    ]
