# Generated by Django 5.0.4 on 2024-04-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(max_length=20)),
                ('delivery_address', models.CharField(max_length=20)),
                ('total_distance', models.IntegerField()),
                ('total_population', models.IntegerField()),
                ('village_head', models.CharField(max_length=20)),
            ],
        ),
    ]