"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""


def fibonacci(n):
    """Calcula a sequencia de Fibbonaci, considerando 'n' como o termo da sequencia a ser procurado"""
    pertence_sequencia = f'O valor {termo} não pertence a sequencia de Fibonnaci'
    a = 0 # O valor atual da sequencia
    b = 1 # O valor seguinte da sequencia
    # Durante o loop "a" recebe o valor de "b", e "b" recebe o valor da soma a + b
    
    for i in range(n):
        # Verifica se a + b é igual a soma do termo da sequencia, caso seja igual 
        # significa que o termo procurado é também um dos números da sequencia
        if n == 0:
            pertence_sequencia = f'O valor {n} pertence a sequencia de Fibonnaci e sua posição é a 0º' # Informa o número e a posição na sequencia de Fibonacci
        elif a + b == n:
            if n == 1:
                pertence_sequencia = f'O valor {n} pertence a sequencia de Fibonnaci e sua posição é a 1º e também está presente na 2º'
            else:
                pertence_sequencia = f'O valor {n} pertence a sequencia de Fibonnaci e sua posição é a {i+2}º' # Informa o número e a posição na sequencia de Fibonacci
        a, b = b, a + b # Troca o valor de a e b

    return a, pertence_sequencia

print('===============================================\n      Calculadora sequencia de Fibonnaci\n')
print("Considerando que a sequencia onde 0 é igual a F0 (posicao 0º), 1 é F1 posicao (posicao 1º)...")
while True:
    print('\n===============================================\n')
    termo = int(input('Informe o termo que deseja consultar: '))
    resultado, pertence_sequencia = fibonacci(termo)
    print(f'\nO resultado da sequencia de Fibonnaci do {termo}º termo é: {resultado}')
    print(pertence_sequencia)
    continuar = input('\nDeseja sair? [S/N]').lower()
    if continuar in ['s', 'sim']:
        break
