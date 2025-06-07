import csv
import datetime


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Превращает объект datetime в строку.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output):
    with open(source_log, 'r') as file_for_read:
        list_log = list(csv.reader(file_for_read))
        head = list_log[0]
        del list_log[0]

        for row in list_log:
            row[2] = convert_str_to_datetime(row[2])

        sorted_data = sorted(list_log, key=lambda x: x[2])[::-1]

        em_list_can = []
        actual_list = []
        for row in sorted_data:
            _email = row[1]
            if _email not in em_list_can:
                em_list_can.append(row[1])
                actual_list.append(row)
            else:
                continue

        for row in actual_list:
            row[2] = convert_datetime_to_str(row[2])

    with open(output, 'w', newline='') as file_for_write:
        writer = csv.writer(file_for_write)
        writer.writerow(head)
        for row in actual_list:
            writer.writerow(row)


write_last_log_to_csv('mail_log.csv', 'actual_mail.csv')
