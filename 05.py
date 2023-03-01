"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""


def inverter_string_slice(string_original):
    return string_original[::-1]


def inverter_string_loop(string_original):
    string_invertida = ''
    for caractere in string_original:
        string_invertida = caractere + string_invertida
    return string_invertida
    

while True:
    string_inicial = input('Digite uma string para inverter: ')
    print(f'\nString Orginal:\n{string_inicial}')
    print(f'\nString invertida usando slice:\n{inverter_string_slice(string_inicial)}')
    print(f'\nString invertida usando loop:\n{inverter_string_loop(string_inicial)}')
    continuar = input('\n\nDeseja sair? [s/n]').lower()
    if continuar in ['s', 'sim']:
        break
