words = ['разработка', 'сокет', 'декоратор']
for word in words:
    print(word, type(word))
unicode_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
                 '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
print('*' * 25)
for unicode_word in unicode_words:
    print(unicode_word, type(unicode_word))
