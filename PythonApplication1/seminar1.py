# ex. 1.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
ans_nat = nat.replace("FastEthernet", "GigabitEthernet")
print(ans_nat)

# ex. 1.2
mac = "AAAA:BBBB:CCCC"
ans_mac = mac.replace(":", ".")
print(ans_mac)

# ex. 1.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
commands = config.split()
vlans13 = commands[4].split(',')
print(vlans13)

# ex. 1.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans = sorted(set(vlans))
print(vlans)

# ex. 1.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command11 = command1.split()[-1].split(',')
command12 = command2.split()[-1].split(',')

l1 = len(command11)
l2 = len(command12)
com = []

for i in command11:
    for j in command12:
        if i == j:
            com.append(i)

print(com)

# ex. 1.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.strip()

piece = ospf_route.split()

route_info = {
    "Prefix": piece[0],
    "AD/Metric": piece[1].strip('[]'),  
    "Next-Hop": piece[3].rstrip(','),   
    "Last update": piece[4].rstrip(','),  
    "Outbound Interface": piece[5],
}

output = f"""
Prefix                {route_info["Prefix"]}
AD/Metric             {route_info["AD/Metric"]}
Next-Hop              {route_info["Next-Hop"]}
Last update           {route_info["Last update"]}
Outbound Interface    {route_info["Outbound Interface"]}
"""

print(output)

# ex. 1.7
mac = "AAAA:BBBB:CCCC"

mac = mac.replace(':', '')
bmac = ''

for c in mac:
    bc = bin(ord(c))[2:]
    bmac += bc
print(bmac)

# ex. 1.8
ip = "192.168.3.1"

ip = ip.split('.')

bip = []
for byte in ip:
    bc = format(int(byte), '08b')
    bip.append(bc)

print("{:<10} {:<10} {:<10} {:<10}".format(*ip))
print("{:<10} {:<10} {:<10} {:<10}".format(*bip))

# ex. 2.1
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

cisco_mac = []

for address in mac:
    cisco_address = address.replace(':', '.')
    cisco_address = cisco_address.upper()
    cisco_mac.append(cisco_address)

print(cisco_mac)

# ex. 2.2 / 2.2a
ip = input()

bytes = ip.split('.')

gate = True

if len(bytes) != 4:
    gate = False
else:
    for byte in bytes:
        if not byte.isdigit() or not 0 <= int(byte) <= 255:
            gate = False
            break


if not gate:
    print("Неправильный IP-адрес")
else:
    first_byte = int(bytes[0])

    if ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    elif 1 <= first_byte <= 223:
        print("unicast")
    elif 224 <= first_byte <= 239:
        print("multicast")
    else:
        print("unused")
        
# # ex. 2.3
while True:
    ip = input()

    bytes = ip.split('.')

    gate = True

    if len(bytes) == 4:
        
        for byte in bytes:
            if byte.isdigit() or 0 <= int(byte) <= 255:
                break

    print("Неправильный IP-адрес")

        

first_byte = int(bytes[0])

if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= first_byte <= 223:
    print("unicast")
elif 224 <= first_byte <= 239:
    print("multicast")
else:
    print("unused")

# ex. 2.4
trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"]
}

for intf, vlan_list in trunk.items():
    print(f"interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = vlan_list[0] 
            vlans = ",".join(vlan_list[1:])
            
            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
        else:
            print(f" {command}")