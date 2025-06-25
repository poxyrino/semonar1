import sqlite3
import sys
from tabulate import tabulate

db_name = 'dhcp_snooping.db'
args = sys.argv[1:]

def get_all_dhcp_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dhcp")
    data = cursor.fetchall()
    conn.close()
    return data


def get_filtered_dhcp_data(db_name, key, value):
    valid_keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key not in valid_keys:
        print(f"Данный параметр не поддерживается.")
        print(f"Допустимые значения параметров: {', '.join(valid_keys)}")
        return None

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dhcp WHERE {key} = ?", (value,))
    data = cursor.fetchall()
    conn.close()
    return data


def print_dhcp_data(data, header=None):
    if not data:
        print("Нет данных для отображения")
        return

    headers = ["mac", "ip", "vlan", "interface", "switch"]
    print(tabulate(data, headers=headers, tablefmt="grid"))





if len(args) == 0:
    print("В таблице dhcp такие записи:")
    data = get_all_dhcp_data(db_name)
    print_dhcp_data(data)
elif len(args) == 2:
    key, value = args
    print(f"Информация об устройствах с такими параметрами: {key} {value}")
    data = get_filtered_dhcp_data(db_name, key, value)
    if data is not None:
        print_dhcp_data(data)
else:
    print("Пожалуйста, введите два или ноль аргументов")


