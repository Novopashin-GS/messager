def string_to_byte(*args):
    for word in args:
        encode_word = word.encode('utf-8')
        print(encode_word)
        decode_word = encode_word.decode('utf-8')
        print(decode_word)
        print('*' * 25)


string_to_byte('разработка', 'администрирование', 'protocol', 'standard')
