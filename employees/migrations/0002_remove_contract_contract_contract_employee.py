# Generated by Django 5.0.6 on 2024-05-24 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='contract',
        ),
        migrations.AddField(
            model_name='contract',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='employees.employee'),
            preserve_default=False,
        ),
    ]
