import yaml

DATA_IN = {'items': ['книга', 'машина', 'phone', 'mouse'],
           'items_quantity': 4,
           'items_price': {'книга': '1€-10€',
                           'машина': '1000€-3000€',
                           'phone': '100€-500€',
                           'mouse': '4€-7€'}
           }
with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
