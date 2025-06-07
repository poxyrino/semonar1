# ex. 1.1
'''
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

ent = input('Введите имя устройства: ')
if ent in london_co:
    print(london_co[ent])
'''


# ex. 1.1a
'''
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

ent1 = input('Введите имя устройства: ')
ent2 = input('Введите имя параметра: ')

if london_co[ent1][ent2]:
    result = london_co[ent1][ent2]
    print(result)
else:
    print("Указанное устройство или параметр не найдены.")
'''


# ex. 1.1b
'''
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

ent1 = input('Введите имя устройства: ')

parameters_list = list(london_co.get(ent1, {}).keys())
parameters_str = ', '.join(parameters_list)

ent2 = input(f'Введите имя параметра({parameters_str}): ')

if london_co[ent1][ent2]:
    result = london_co[ent1][ent2]
    print(result)
else:
    print("Указанное устройство или параметр не найдены.")
'''


# ex. 1.1c
'''
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

ent1 = input('Введите имя устройства: ')

parameters_list = list(london_co.get(ent1, {}).keys())
parameters_str = ', '.join(parameters_list)


ent2 = input(f'Введите имя параметра({parameters_str}): ')

try:
    ent2 in parameters_str
    if london_co[ent1][ent2]:
        result = london_co[ent1][ent2]
        print(result)
    else:
        print("Указанное устройство или параметр не найдены.")
except:
    print('Такого параметра нет')
'''



# ex. 1.1d
'''
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

ent1 = input('Введите имя устройства: ')

parameters_list = list(london_co.get(ent1, {}).keys())
parameters_str = ', '.join(parameters_list).lower()

ent2 = input(f'Введите имя параметра({parameters_str}): ')
ent2 = ent2.lower()

try:
    ent2 in parameters_str
    if london_co[ent1][ent2]:
        result = london_co[ent1][ent2]
        print(result)
    else:
        print("Указанное устройство или параметр не найдены.")
except:
    print('Такого параметра нет')
'''

# ex. 1.2 (НЕ ДОДЕЛАНО!!!)
"""
ip = input('Введите IP-сети в формате: 10.1.1.0/24: ')
ip = ip.replace('/', '.')
ip = ip.split('.')

mask = ip[-1:]
ip = ip[:-1]

bip = []
for byte in ip:
    bc = format(int(byte), '08b')
    bip.append(bc)

print(f'''Network:
{"{:<10} {:<10} {:<10} {:<10}".format(*ip)}  
{"{:<10} {:<10} {:<10} {:<10}".format(*bip)}
''')

c_mask = int(mask[0])
bin_mask = c_mask * '1' + (32 - c_mask) * '0'

bmask = []
emask = []
for byte in range(4):
    bc = bin_mask[byte * 8 : (byte + 1) * 8]
    bmask.append(bc)
    be = str(int(bc, 2))
    emask.append(be)

print(f'''Mask: 
/{mask[0]}
{"{:<10} {:<10} {:<10} {:<10}".format(*emask)}
{"{:<10} {:<10} {:<10} {:<10}".format(*bmask)}
''')
"""


# ex. 1.2a
"""
ip = input('Введите адрес хоста в формате: 10.1.1.1/24: ')
ip = ip.replace('/', '.')
ip = ip.split('.')

mask = ip[-1:]
ip = ip[:-1]
ip[-1] = '0'

bip = []
for byte in ip:
    bc = format(int(byte), '08b')
    bip.append(bc)

print(f'''Network:
{"{:<10} {:<10} {:<10} {:<10}".format(*ip)}  
{"{:<10} {:<10} {:<10} {:<10}".format(*bip)}
''')

c_mask = int(mask[0])
bin_mask = c_mask * '1' + (32 - c_mask) * '0'

bmask = []
emask = []
for byte in range(4):
    bc = bin_mask[byte * 8 : (byte + 1) * 8]
    bmask.append(bc)
    be = str(int(bc, 2))
    emask.append(be)

print(f'''Mask: 
/{mask[0]}
{"{:<10} {:<10} {:<10} {:<10}".format(*emask)}
{"{:<10} {:<10} {:<10} {:<10}".format(*bmask)}''')
"""

# ex. 1.3
"""
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(f"interface {interface}")
if mode == "access":
    for command in access_template:
        print(command.format(vlans))
elif mode == "trunk":
    for command in trunk_template:
        print(command.format(vlans))
"""

# ex. 1.3a

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")

if mode == "access":
    print(f"interface {interface}")
    vlans = input('Введите номер VLAN: ')
    for command in access_template:
        print(command.format(vlans))
elif mode == "trunk":
    print(f"interface {interface}")
    vlans = input('Введите разрешенные VLAN: ')
    for command in trunk_template:
        print(command.format(vlans))

