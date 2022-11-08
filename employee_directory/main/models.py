from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Departments(MPTTModel):
    # Making unique name, and increase speed of finding this field.
    name = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='Название')
    slug = models.SlugField()
    # Making a department depth. Accept Null for ForeignKey, accept Blank for parents Department.
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                            verbose_name='Подразделение родитель')

    class MPTTMeta:
        order_insertion_by = ['name']  # By which field to sort children's in tree.

    class Meta:
        unique_together = ['parent', 'slug']  # Make fields parents and slug unique.
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def get_absolute_url(self):  # The method to create a small canonical URL for an object.
        return reverse('employee-at-department', args=[str(self.slug)])

    MAX_TREE_DEPTH = 4

    def clean(self):  # The method can create Department depth up to 5 levels.
        self.parent_foo = self.parent
        if self.parent_foo is None:
            parent_level = 0
        else:
            parent_level = self.parent_foo.get_level()
        if parent_level + 1 > self.MAX_TREE_DEPTH:
            raise ValidationError({'parent': f"Подразделения имеют структуру до "
                                             f"{self.MAX_TREE_DEPTH + 1} уровней"})

    def __str__(self):
        return self.name


class Employees(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='ФИО')
    position = models.CharField(max_length=150, verbose_name='Должность')
    emp_date = models.DateField(verbose_name='Дата приёма на работу')
    salary = models.IntegerField(verbose_name='Размер заработной платы')
    slug = models.SlugField(max_length=150)
    # ForeignKey to connect with models.Departments, PROTECTED to save obj.Employees from delete with obj.Departments.
    department = TreeForeignKey('Departments', on_delete=models.PROTECT, verbose_name='Подразделение')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


