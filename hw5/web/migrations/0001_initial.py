# Generated by Django 5.0.3 on 2024-04-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('birth', models.DateTimeField()),
                ('intro', models.TextField()),
                ('elite', models.BooleanField(default=False)),
                ('live', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
