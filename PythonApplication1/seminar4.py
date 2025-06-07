"""
# ex. 1.1/1.1a
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    _list = []
    for key, value in intf_vlan_mapping.items():
        _list.append("interface " + key)
        for template in access_template:
            if "switchport access vlan" in template:
                _list.append("switchport access vlan" + " " + str(value))
            else:
                _list.append(template)

    if psecurity != None:
        for psec in psecurity:
            _list.append(str(psec))

    return _list


generate_access_config(access_config, access_mode_template)
generate_access_config(access_config, access_mode_template, port_security_template)

# ex. 1.2/1.2a
trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_configuration = {}
    for interface, vlans in intf_vlan_mapping.items():
        interface_commands = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlan_str = ",".join(str(vlan) for vlan in vlans)
                interface_commands.append(f"{command} {vlan_str}")
            else:
                interface_commands.append(command)
        trunk_configuration[interface] = interface_commands
    return trunk_configuration


print(generate_trunk_config(trunk_config, trunk_mode_template))
"""
from traceback import print_tb


# ex. 1.3/1.3a
"""
def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}

    with open(config_filename, 'rt') as file:
        interface = None
        for line in file:
            parts = line.split()
            if not parts:
                continue
            if parts[0] == 'interface':
                interface = parts[1]
            elif 'switchport mode access' in line:
                access[interface] = 1
            elif 'switchport access vlan' in line:
                vlan = int(parts[-1])
                access[interface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                vlans = list(map(int, parts[-1].split(',')))
                trunk[interface] = vlans
            elif 'switchport mode trunk' in line and interface not in trunk:
                trunk[interface] = []

    return access, trunk
"""
# ex. 1.4

def ignore_command(command, ignore):
    for word in ignore:
        if word in command:
            return True
    return False


def convert_config_to_dict(config_filename):
    ignore_words = ["duplex", "alias", "Current configuration"]
    config_dict = {}
    current_key = None

    with open(config_filename, 'rt') as file:
        for line in file:
            line = line.rstrip('\n')  # Сохраняем начальные пробелы
            stripped_line = line.strip()

            # Пропускаем пустые строки и комментарии
            if not stripped_line or line.startswith('!'):
                continue

            # Проверяем на игнорируемые команды
            if ignore_command(stripped_line, ignore_words):
                continue

            # Обработка команд верхнего уровня и подкоманд
            if not line.startswith(' '):
                current_key = stripped_line
                config_dict[current_key] = []
            else:
                if current_key is not None:
                    config_dict[current_key].append(stripped_line)

    return config_dict

print(convert_config_to_dict("config_sw2_4.txt"))