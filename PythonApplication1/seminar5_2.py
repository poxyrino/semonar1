import csv
import re
import glob

sh_version = glob.glob("sh_version_r*.txt")


def parse_sh_version(version):
    ios_dry = r"Cisco IOS Software, (\d{4}) Software (\S+), Version (\S+),"
    ios_match = re.search(ios_dry, version)
    ios = ios_match.group(3)

    image_dry = r'System image file is "(.+)"'
    image_match = re.search(image_dry, version)
    image = image_match.group(1)

    uptime_dry = r"router uptime is (.+)"
    uptime_match = re.search(uptime_dry, version)
    uptime = uptime_match.group(1)

    return (ios, image, uptime)


def write_inventory_to_csv(data_filenames, csv_filename):
    with open(csv_filename, 'w', newline='') as file_writing:
        writer = csv.writer(file_writing)

        head = ['hostname', 'ios', 'image', 'uptime']
        writer.writerow(head)

        for filename in data_filenames:
            match = re.search(r"sh_version_(\w+)\.txt", filename)
            hostname = match.group(1)

            with open(filename, 'r') as file:
                content = file.read()

            ios, image, uptime = parse_sh_version(content)

            writer.writerow([hostname, ios, image, uptime])


write_inventory_to_csv(sh_version, "output_for_ex2.csv")
