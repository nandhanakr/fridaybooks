# Generated by Django 5.0.1 on 2024-02-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
