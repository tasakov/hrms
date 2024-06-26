# Generated by Django 5.0.6 on 2024-06-05 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_education_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('skill_type', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
