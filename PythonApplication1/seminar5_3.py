import re
import glob
import yaml


def parse_sh_cdp_neighbors(content):
    data = {}

    R_dry = r"(\w+\d+)>show cdp neighbors"
    R_match = re.search(R_dry, content)
    if not R_match:
        return {}

    R = R_match.group(1)
    data[R] = {}

    neighbor_dry = r'^(\S+)\s+(\S+ \S+)\s+\d+\s+[R S I]+\s+\S+\s+(\S+ \S+)$'

    for line in content.split('\n'):
        line = line.strip()

        neighbor_match = re.match(neighbor_dry, line)
        if neighbor_match:
            neighbor_dev = neighbor_match.group(1)
            neighbor_LocalInterface = neighbor_match.group(2)
            neighbor_PortID = neighbor_match.group(3)

            data[R][neighbor_LocalInterface] = {neighbor_dev: neighbor_PortID}
    return data


"""# Проверка ex. 1.3
if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt", "r") as f:
        content = f.read()
    result = parse_sh_cdp_neighbors(content)
    print(result)
"""


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    data = {}

    for filename in list_of_files:
        with open(filename, 'r') as file_in:
            content = file_in.read()
        parse_data = parse_sh_cdp_neighbors(content)
        data.update(parse_data)

    with open(save_to_filename, 'w') as file_out:
        yaml.dump(data, file_out, default_flow_style=False)

    return data


sh_cdp = glob.glob("sh_cdp_n_*.txt")

print(generate_topology_from_cdp(sh_cdp, "sh_cdp.yaml"))


def transform_topology(file_yaml):
    topology_data = {}
    with open(file_yaml) as file:
        topology_dict = yaml.safe_load(file)
        for local_device, neighbors in topology_dict.items():  # .items() возвращает представление всех пар ключ-значение
            for local_port, remote_info in neighbors.items():
                remote_device, remote_port = next(iter(remote_info.items()))

                # remote_info.items() возвращает пары ключ-значение словаря.
                # Например, для {"R5": "Fa 0/1"} вернёт dict_items([('R5', 'Fa 0/1')]).
                # iter() создаёт итератор из этих пар.
                # next() извлекает первую (и единственную) пару из этого итератора:'''

                connection1 = (local_device, local_port)
                connection2 = (remote_device, remote_port)

                if connection2 not in topology_data:
                    topology_data[connection1] = connection2
    return topology_data


draw_data = transform_topology("sh_cdp.yaml")
print(draw_data)
