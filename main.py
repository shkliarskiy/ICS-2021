"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файл
показує на екрані первинні дані
"""

<<<<<<< HEAD
=======
#from process_data import create_zajavka

>>>>>>> group-5
from process_data import create_zajavka
from data_service import show_clients, show_orders, get_orders, get_clients
import os

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ЗЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід довідника клієнтів
0 - завершити роботу
-----------------------------
"""

TITLE = "ЗАЯВКИ НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ"
HEADER = \
'''
===========================================================================================
| Устаткування      |   Клієнт           |  Номер заказа  | Кількість |   Ціна   |  Сума  |
===========================================================================================
'''
FOOTER = \
'''
===========================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"

def show_zajavka(zajavka_list):
    """виводить сформовані заявки на екран у вигляді таблиці

    Args:
        zajavka_list ([type]): список заявок
    """
    
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['oborud']:20}",
              f"{zajavka['client']:20}",
              f"{zajavka['zakaz']:^15}",
              f"{zajavka['kol']:>12}"
              f"{zajavka['price']:>10.2f}"
              f"{zajavka['total']:>11.2f}"
              )
    
    print(FOOTER)


def write_zajavka(zajavka_list):
    """пише список заявок у файл

    Args:
        zajavka_list ([type]): список заявок
    """
    
    with open('./data/zajavki.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = \
                zajavka['oborud'] + ';' +      \
                zajavka['client'] + ';' +      \
                zajavka['zakaz']  + ';' +      \
                str(zajavka['kol'])  + ';' +   \
                str(zajavka['price'])  + ';' + \
                str(zajavka['total']) + '\n' 
                
            zajavka_file.write(line)
        
        print("Файл заявок сформовано ...")
    

while True:
    
    # вивід головного меню
    os.system('clear')
    print (MAIN_MENU)
    command_number = input('Введіть номер команди: ')

    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        zajavka_list = create_zajavka()
<<<<<<< HEAD
        # show_zajavka(zajavka_list)
=======
>>>>>>> group-5
        show_zajavka(create_zajavka())
        input(STOP_MESSAGE)
    
    elif command_number == '2':
        zajavka_list = create_zajavka()
        write_zajavka(zajavka_list)
        input(STOP_MESSAGE)
    
    elif command_number == '3':
        show_orders(get_orders())
        input(STOP_MESSAGE)
    
    elif command_number == '4':
        show_clients(get_clients())
        input(STOP_MESSAGE)
        
    else:
        print("невірний номер команди...")
        input(STOP_MESSAGE)


    
    
    
