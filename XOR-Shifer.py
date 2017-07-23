
import itertools
def XOR_cipher(string, key):
    answer = [] #кортеж
    key = itertools.cycle(key) # повтор ключа для зашивровки всего sring
    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))
    return ''.join(answer)
string = input('Логин: ')
key = input('Пароль: ')
print(XOR_cipher(string, key))
