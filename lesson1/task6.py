import chardet

with open('test_file.txt', 'w', encoding='cp1251') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')


def get_encoding(file_name):
    with open(file_name, 'rb') as f2:
        content = f2.read()
        encoding = chardet.detect(content)['encoding']
        return encoding


def open_file(file_name):
    encoding = get_encoding(file_name)
    with open(file_name, 'r', encoding=encoding) as f3:
        for line in f3:
            print(line.strip())


open_file('test_file.txt')
