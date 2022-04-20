def string_to_byte(*args):
    for word in args:
        byte_word = eval(f'b"{word}"')
        print(byte_word, type(byte_word))


string_to_byte('class', 'function', 'method')
