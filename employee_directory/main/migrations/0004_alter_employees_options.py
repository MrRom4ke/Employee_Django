# Generated by Django 4.1.2 on 2022-10-30 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_departments_name_alter_departments_parent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ['name'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
    ]
