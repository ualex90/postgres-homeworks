import csv
from pathlib import Path

import psycopg2

from settings import USER_NAME, PASSWORD, NORTH_DATA

"""Скрипт для заполнения данными таблиц в БД Postgres."""


def load_csv(file) -> list[dict]:
    """Читает СSV файл и возвращает список словарей"""
    with open(file, 'r', encoding='UTF-8') as f:
        items: csv.DictReader = csv.DictReader(f)
        csv_data = list(items)
    return csv_data


def get_lines(data) -> list[tuple]:
    """Преобразует список словарей в список картежей"""
    lines = list()
    for line in data:
        lines.append(tuple(line.values()))
    return lines


# Получаем списки словарей изх файла
employees_data = load_csv(Path(NORTH_DATA, 'employees_data.csv'))
customers_data = load_csv(Path(NORTH_DATA, 'customers_data.csv'))
orders_data = load_csv(Path(NORTH_DATA, 'orders_data.csv'))

# Преобразуем списки словарей в списки картежей
employees = get_lines(employees_data)
customers = get_lines(customers_data)
orders = get_lines(orders_data)

# Подключение и заполнение базы данных
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user=USER_NAME,  # из переменной окружения
    password=PASSWORD  # из переменной окружения
)
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees)
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers)
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders)
finally:
    conn.close()
