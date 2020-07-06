# Generated by Django 3.0.2 on 2020-07-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolClass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name_subclass',
            field=models.CharField(blank=True, help_text="Name of a subclass, ex 'A', 'B', '1', '2', ...", max_length=50, null=True, verbose_name='SubClass'),
        ),
    ]
