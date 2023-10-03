# Generated by Django 3.2.12 on 2023-09-29 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oilfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OperationalUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('oilfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explorer.oilfield')),
            ],
        ),
        migrations.AddField(
            model_name='oilfield',
            name='operational_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explorer.operationalunit'),
        ),
    ]
