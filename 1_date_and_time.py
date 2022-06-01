"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime

def print_days():
    dt_now = date.today()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_30_days_ago = dt_now - timedelta(days=30)
    print('Вчера:', dt_now.strftime('%d.%m.%Y'))
    print('Сегодня:', dt_yesterday.strftime('%d.%m.%Y'))
    print('30 дней назад:', dt_30_days_ago.strftime('%d.%m.%Y'))
    return 0

def str_2_datetime(date_string):
    dt_transformation = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt_transformation

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
