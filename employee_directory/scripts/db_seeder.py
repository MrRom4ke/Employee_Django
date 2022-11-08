from django_seed import Seed
from faker import Faker
import random
from slugify import slugify

from main.models import Employees, Departments


def first_dep():
    dep = Departments(
        name='Рога и копыта',
        slug='roga-i-kopyta',
    )
    dep.save()
    global first_parent_id
    first_parent_id = Departments.objects.all()[0].id


def fill_dep(count, id_min, id_max):
    seeder = Seed.seeder()
    fake = Faker('ru_RU')
    with Departments.objects.disable_mptt_updates():
        seeder.add_entity(Departments, count, {
            'name': lambda x: "Отдел " + fake.bs(),
            'parent': lambda x: Departments.objects.get(
                id=random.randint((first_parent_id + id_min), (first_parent_id + id_max))
            ),
        })
        seeder.execute()


def fill_emp(count, pos, year, salary, id_min, id_max):
    seeder = Seed.seeder()
    fake = Faker('ru_RU')
    seeder.add_entity(Employees, count, {
        'name': lambda x: fake.name(),
        'position': pos,
        'emp_date': '{}-{}-{}'.format(year, random.randint(1, 12), random.randint(1, 28)),
        'salary': lambda x: random.randint(salary-9000, salary+9000),
        'department': lambda x: Departments.objects.get(
            id=random.randint((first_parent_id + id_min), (first_parent_id + id_max))
        ),
    })
    seeder.execute()


def del_obj():
    with Employees.objects.disable_mptt_updates():
        objs = Employees.objects.all()
        objs.delete()
    Employees.objects.rebuild()


def run():
    first_dep()
    fill_dep(2, 0, 0)
    fill_dep(4, 1, 2)
    fill_dep(5, 3, 6)
    fill_dep(7, 7, 11)
    fill_dep(7, 11, 18)
    Departments.objects.rebuild()
    fill_emp(2, 'Заместитель начальника', 2010, 200000, 1, 2)
    fill_emp(100, 'Начальник управления', 2012, 170000, 1, 10)
    fill_emp(1000, 'Начальник отдела', 2015, 120000, 1, 25)
    fill_emp(40000, 'Главный эксперт', 2018, 90000, 1, 25)   # about 5 minutes
    fill_emp(10000, 'Ведущий эксперт', 2020, 70000, 1, 25)     # 3.5 minutes
    pass
