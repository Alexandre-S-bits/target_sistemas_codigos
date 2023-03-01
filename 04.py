"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""


fatuamentos_estados = {'SP' : 'R$67.836,43',
'RJ': 'R$36.678,66',
'MG': 'R$29.229,88',
'ES' : 'R$27.165,48',
'Outros' : 'R$19.849,53'}


# Resolvi criar uma função a mais para não alterar os dados base que foram passados (Poderia manipular manualmente e já coloca-los do tipo float)
def converter_para_float():
    lista_valores = []
    for valor in fatuamentos_estados.values():
        valor = float(valor[2:].replace('.','').replace(',', '.'))
        lista_valores.append(valor)
    return lista_valores


def imprimir_informacoes():
    valores = converter_para_float()
    total_faturamento = sum(converter_para_float())
    print('\nRepresentação dos faturamentos da distribuidora por Estado\n--------------------------------------------------------------')
    print(f'Valor total de faturamento: R${total_faturamento:.2f}')
    i = 0
    print(f'\nValor faturamento | Estado | Representação aproximada (%)')
    print(f'------------------|--------|-----------------------------')

    for k, v in fatuamentos_estados.items():
        print(f'{v:^18}|{k:^8}| {(valores[i] * 100 / total_faturamento):.2f}%')
        i += 1


imprimir_informacoes()