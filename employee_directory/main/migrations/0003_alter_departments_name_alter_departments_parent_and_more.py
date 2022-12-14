# Generated by Django 4.1.2 on 2022-10-25 15:48

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_departments_employees_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.departments', verbose_name='Подразделение родитель'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.departments', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='emp_date',
            field=models.DateField(verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=150, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='position',
            field=models.CharField(max_length=150, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(verbose_name='Размер заработной платы'),
        ),
    ]
