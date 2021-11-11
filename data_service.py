# модуль призначено для роботи з зовнішніми файлами
# чітання та виведення для візуального контролю


def get_clients():
    """читання файлу кліентіів `clients`
    та фрмування списку клієнтів
    повертає список клієнтів
    """
    
    # накопичення даних файлу у списку
    with open("./data/clients.csv", 'r')  as f:
        clients = f.readlines()
        
    # підгтовка даних для подальшої обробки
    cliens_splitted = []
    # порізати в циклі строки на окремі єлементи 
    for client in clients:
        obj = split_line(client)
        obj[0] = int(obj[0])
        cliens_splitted.append(obj)

    return cliens_splitted

def split_line(line):
    """повертає спісок обєктів з строки"""
    object = line.split(',')
    return object

# читання файлу кліентіів `orders`
def get_orders():
    """читання файлу накладних `orders`
    та фрмування списку накладних
    повертає список накладних
    """
    # накопичення даних файлу у списку
    with open("./data/orders.csv", 'r')  as f:
        orders = f.readlines()
        
    # підгтовка даних для подальшої обробки
        orders_splitted = []
        # порізати в циклі строки на окремі єлементи 
        for order in orders:
            obj = split_line(order)
            orders_splitted.append(obj)

    return orders_splitted

    

# вивід списку кліетів
def show_clients(clients):
    """вивдить список клієтів по заданоому інтервалу кодів
    """

    #  задати інтервал кодів
    client_code_from = int(input("З якого кода клієнта? "))
    client_code_to   = int(input("До якого кода клієнта? "))
    
    # відбір  списку клієнтів 
    filtered_clients = []
    for client in clients:
        if client_code_from <= client[0] <= client_code_to:
            filtered_clients.append(client)
            
    if len(filtered_clients) == 0:
        print("В списку клієнтів нема таких кодів")
        return
    
    
    # вивід відібраного списку
    print("СПИСОК КЛІЄНТІВ")
    for client in filtered_clients:
        print(f'код клієнта: {client[0]:3} назва: {client[1]:20} адреса: {client[2][:-1]:25}')
    
    
    

# вивід списку накладних


if __name__ == '__main__':  
    clients = get_clients()
    orders  = get_orders()
    
    rc = show_clients(clients)
    pass   