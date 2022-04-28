import chardet
import re
import csv


def get_data():
    os_manufacturer_list = []
    os_name_list = []
    product_code_list = []
    system_type_list = []
    main_data = []
    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as f:
            data_bytes = f.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])
            os_manufacturer_list.append((re.search(r'Изготовитель системы:\s+(\S+)', data)).group(1))
            os_name_list.append((re.search(r'Название ОС:\s+(.+)\r', data)).group(1))
            product_code_list.append((re.search(r'Код продукта:\s+(\S+)', data)).group(1))
            system_type_list.append((re.search(r'Тип системы:\s+(.+)\r', data)).group(1))
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)
    sum_data = [os_manufacturer_list, os_name_list, product_code_list, system_type_list]
    for i in range(len(headers) - 1):
        row = []
        for item in sum_data:
            row.append(item[i])
        main_data.append(row)
    print(main_data)
    return main_data


def write_to_csv():
    with open('test.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(get_data())


write_to_csv()
