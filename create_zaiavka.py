""" Модль призначено для формування заявки ...
яка формується з фапйлів 'clients` та `orders`"""

from data_service import get_clients, get_orders

TITLE = "\n\nЗАЯВКИ НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""  
=============================================================================
Устаткування      :  Клієнт   : Заказ  : Кількість   : Ціна   :      Сума 
=============================================================================
"""

orders = get_orders()
clients = get_clients()

def find_client_name(client_code):
    """шукає в довіднику назву клієнта по його коду"""
    
    for client in clients:
        if client_code == client[0]:
            return client[1]
    
    return "нема назви"   

def str_to_num(str_num):
    """перетворює строкове чісло в число""" 
    if str_num.isnumeric():
        return float(str_num)
    else:
        return float(str_num[:-1])
 
def show_zajavka(zajavki):
    """"вивід результатів на екран"""
    print(TITLE)
    print(HEADER)
    for row in zajavki:
        print(f"{row['oborud']:20}",
                f"{row['client']:14}", 
                f"{row['zakaz']:8}", 
                f"{row['kol']:10}",
                f"{row['price']:10}",
                f"{row['total']:10.2f}"
          ) 

   

# zajavka = {
#     'oborud' : "",     # назва устаткування     (orders)
#     'client' : "",     # назва клієнта          (clients)
#     'zakaz'  : "",     # номер заказа           (orders)
#     'kol'    : 0,      # кількість товару       (orders)
#     'price'  : 0.0,    # ціна                   (orders)
#     'total'  : 0.0     # сума                   (price * kol)
# }

zajavkas = []

for order in orders:
    
    zajavka = {
        'oborud': "",   # назва устаткування     (orders)
        'client': "",   # назва клієнта          (clients)
        'zakaz': "",    # номер заказа           (orders)
        'kol': 0,       # кількість товару       (orders)
        'price': 0.0,   # ціна                   (orders)
        'total': 0.0    # сума                   (price * kol)
    }

    zajavka['oborud'] = order[2]
    zajavka['zakaz']  = order[1]
    zajavka['kol']    = order[3]
    zajavka['price']  = str_to_num(order[4])
    zajavka['total']  = str_to_num(order[3]) * str_to_num(order[4])
    zajavka['client'] = find_client_name(str_to_num(order[0]))
    
    zajavkas.append(zajavka)
    

show_zajavka(zajavkas)
