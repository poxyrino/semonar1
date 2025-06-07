# ex. 1.1
"""
with open('ospf.txt', 'rt') as ospfTXT:
    list = []
    for line in ospfTXT:
        list.append(line)

for block in list:
    piece = block.split()

    _info = f'''
        Prefix              {piece[1]}
        AD/Metric           {piece[2].strip('[]')}
        Next-Hop            {piece[4].rstrip(',')}
        Last update         {piece[5].rstrip(',')}
        Outbound Interface  {piece[6]}
        '''
    print(_info)
"""
# ex. 1.2
"""
with open('config_sw1.txt', 'rt') as config_sw1:
    _txt = ''
    for line in config_sw1:
        if str(line)[0] != '!':
            _txt += (str(line.strip()) + '\n')
print(_txt)
"""
# ex. 1.2a
"""
ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt', 'rt') as config_sw1:
    _txt = ''
    for line in config_sw1:
        if str(line)[0] != '!':
            if not any(ignore_wrd in line for ignore_wrd in ignore):
                _txt += (str(line.strip()) + '\n')

print(_txt)
"""
# ex. 1.2b
"""
ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt', 'rt') as config_sw1:
    _txt = ''
    for line in config_sw1:
        if str(line)[0] != '!':
            if not any(ignore_wrd in line for ignore_wrd in ignore):
                _txt += (str(line.strip()) + '\n')
with open('config_sw1_update.txt', 'w') as config_sw1_update:
    config_sw1_update.write(_txt)
"""
# ex. 1.3
"""
_print = ''
with open('CAM_table.txt', 'rt') as CAM_table:
    _list = []
    for line in CAM_table:
        _parts = line.split()
        if len(_parts) > 3:
            mac_parts = _parts[1].split('.')
            if (len(mac_parts) == 3 and
                    len(mac_parts[0]) == 4 and
                    len(mac_parts[1]) == 4 and
                    len(mac_parts[2]) == 4
            ):
                # parts = [_parts[0], _parts[1], _parts[3]]
                # _list.append(parts)
                _print += '{:<7} {:<18} {}\n'.format(
                    _parts[0],
                    _parts[1],
                    _parts[3])
print(_print)
"""

# ex. 1.3a
"""
with open('CAM_table.txt', 'rt') as CAM_table:
    _list = []
    for line in CAM_table:
        _parts = line.split()
        if len(_parts) > 3:
            mac_parts = _parts[1].split('.')
            if (len(mac_parts) == 3 and
                    len(mac_parts[0]) == 4 and
                    len(mac_parts[1]) == 4 and
                    len(mac_parts[2]) == 4
            ):
                parts = [_parts[0], _parts[1], _parts[3]]
                _list.append(parts)
_list.sort(key=lambda x: int(x[0]))
_print = ''
for p in _list:
    _print += '{:<7} {:<18} {}\n'.format(
        p[0],
        p[1],
        p[2])
print(_print)
"""

# ex. 1.3b
with open('CAM_table.txt', 'rt') as CAM_table:
    _list = []
    for line in CAM_table:
        _parts = line.split()
        if len(_parts) > 3:
            mac_parts = _parts[1].split('.')
            if (len(mac_parts) == 3 and
                    len(mac_parts[0]) == 4 and
                    len(mac_parts[1]) == 4 and
                    len(mac_parts[2]) == 4
            ):
                parts = [_parts[0], _parts[1], _parts[3]]
                _list.append(parts)
_list.sort(key=lambda x: int(x[0]))

vlan_num = input('Enter VLAN number: ')

_print = ''
for p in _list:
    if vlan_num == str(p[0]):
        _print += '{:<7} {:<18} {}\n'.format(
            p[0],
            p[1],
            p[2])
print(_print)
