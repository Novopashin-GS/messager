def string_to_byte(*args):
    for word in args:
        try:
            byte_word = eval(f'b"{word}"')
            print(byte_word, type(byte_word))
        except:
            print(f'Слово {word} невозможно записать в байтовом формате')


string_to_byte('attribute', 'класс', 'функция', 'type')
