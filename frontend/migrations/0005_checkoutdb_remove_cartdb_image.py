# Generated by Django 5.0.1 on 2024-02-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_cartdb_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartdb',
            name='Image',
        ),
    ]
