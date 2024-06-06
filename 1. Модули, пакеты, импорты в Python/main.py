from application.salary import list_salaries
from application.db.people import list_people
from datetime import datetime as dt
from faker import Faker


def date_people(region):

    faker = Faker(region)

    name = faker.name()
    birthday = faker.date_of_birth()
    address = faker.address()
    email = faker.email()
    job = faker.job()
    print(f'{name}\n{birthday}\n{address}\n{email}\n{job}\n\n')


if __name__ == '__main__':
    print(f'Текущее время: {dt.now().strftime("%H:%M:%S" + " %d.%m.%Y")}')

    list_salaries()
    list_people()

    region = input('Выберите регион: ').strip() or 'RU'
    count_people = int(input('Введите кол-во людей: ').strip() or '1')
    for reg in range(count_people):
        date_people(region)
