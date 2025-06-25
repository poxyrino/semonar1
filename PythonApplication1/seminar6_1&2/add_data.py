import sqlite3
import yaml
import os

db_name = 'dhcp_snooping.db'
switches_file = 'switches.yml'
dhcp_files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']

def check_db_exists(db_name):
    if not os.path.exists(db_name):
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return False
    return True


def add_switches_data(db_name, switches_file):
    print("Добавляю данные в таблицу switches...")

    with open(switches_file) as f:
        switches = yaml.safe_load(f)['switches']

    connection = sqlite3.connect(db_name)
    for hostname, location in switches.items():
        try:
            with connection:
                connection.execute("INSERT INTO switches values (?, ?)", (hostname, location))
        except sqlite3.IntegrityError as e:
            print(f"При добавлении данных: ('{hostname}', '{location}') Возникла ошибка: {e}")
    connection.close()


def parse_dhcp_snooping(filename):
    result = []
    switch = os.path.basename(filename).split('_')[0]

    with open(filename) as f:
        for line in f:
            if 'MacAddress' in line or '--' in line or not line.strip():
                continue
            parts = line.split()

            if len(parts) >= 6:
                mac = parts[0]
                ip = parts[1]
                vlan = parts[4]
                interface = parts[5]
                result.append((mac, ip, vlan, interface, switch))
    return result


def add_dhcp_data(db_name, dhcp_files):
    print("Добавляю данные в таблицу dhcp...")

    connection = sqlite3.connect(db_name)
    for file in dhcp_files:
        if not os.path.exists(file):
            print(f"Файл {file} не найден, пропускаю...")
            continue

        data = parse_dhcp_snooping(file)
        for row in data:
            try:
                with connection:
                    connection.execute("INSERT INTO dhcp values (?, ?, ?, ?, ?)", row)
            except sqlite3.IntegrityError as e:
                print(f"При добавлении данных: {row} Возникла ошибка: {e}")
    connection.close()



add_switches_data(db_name, switches_file)
add_dhcp_data(db_name, dhcp_files)


