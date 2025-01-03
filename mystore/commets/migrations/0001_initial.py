# Generated by Django 5.1.3 on 2024-12-05 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('elemet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.element')),
            ],
        ),
    ]
