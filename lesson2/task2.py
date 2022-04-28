import json


def write_order_to_json(item, quantity, price, buyer, date):
    try:
        with open('order.json', 'r', encoding='utf-8') as f_out:
            data = json.load(f_out)
    except FileNotFoundError:
        data = []

    with open('order.json', 'w', encoding='utf-8') as f:
        order = {
            'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date
        }
        data.append(order)
        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('сканер', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('компьютер', '5', '40000', 'Сидоров С.С.', '2.05.2019')
