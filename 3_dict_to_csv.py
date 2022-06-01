"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv
from dataclasses import field
from encodings import utf_8

employee = [ 
    {'name': "Дима", 'age': "27", 'job':"МО"},
    {'name': "Коля", 'age': "37", 'job':"ЖКХ"},
    {'name': "Юра", 'age': "22", 'job':"Суд"},
    {'name': "Света", 'age': "18", 'job':"Киоск"},
    ]

def main():

    with open('employee.csv', 'w', encoding="utf_8", newline='') as csv_file:
        fields = ['name','age','job']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()
        for line in employee:
            writer.writerow(line)

if __name__ == "__main__":
    main()
