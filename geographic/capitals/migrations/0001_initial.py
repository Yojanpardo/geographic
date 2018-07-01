# Generated by Django 2.0.5 on 2018-07-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0002_auto_20180701_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='countries.Country')),
            ],
        ),
    ]