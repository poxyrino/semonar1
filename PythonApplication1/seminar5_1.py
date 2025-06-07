import csv
import os
import glob

filenames_input = glob.glob("sw*_dhcp_snooping.txt")
def write_dhcp_snooping_to_csv(filenames, output):
    data = []
    head = ["switch", "mac", "ip", "vlan", "interface"]  # заголовок csv
    data.append(head)

    for filename in filenames:
        base = os.path.splitext(os.path.basename(filename))[0]
        switch_name = base.split('_')[0]


        with open(filename, 'rt') as file_reading:
            lines = file_reading.readlines()

        data_lines = lines[2:-1]

        for line in data_lines:
            line = line.strip()
            parts = line.split()
            mac, ip, _, _, vlan, interface = parts
            data.append([switch_name, mac, ip, vlan, interface])

    with open(output, 'w', newline='') as file_writing:
        writer = csv.writer(file_writing)
        for row in data:
            writer.writerow(row)



write_dhcp_snooping_to_csv(filenames_input,"output_for_ex1.csv")

with open('output_for_ex1.csv') as f:
    print(f.read())
