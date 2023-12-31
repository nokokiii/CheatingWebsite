# Generated by Django 4.2.7 on 2023-12-03 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('unitId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('unitName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('noteId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('noteTitle', models.CharField(max_length=200)),
                ('noteContent', models.TextField()),
                ('unitId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='history.units')),
            ],
        ),
    ]
