"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""


import json


def dados_faturamento():
    with open("dados.json") as arquivo_dados:
        faturamento = json.load(arquivo_dados)
        lista_valores = []
        for valor in faturamento:
            lista_valores.append(valor["valor"])
    return lista_valores


def media_faturamento(dados_faturamento):
    media_faturamento = sum(dados_faturamento) / len(dados_faturamento)
    return media_faturamento


def maior_faturamento(dados_faturamento):
    return max(dados_faturamento)


def menor_faturamento(dados_faturamento):
    return min(dados_faturamento)



def informacoes_faturamento():
    global media
    valores_faturamento = dados_faturamento()

    menor = menor_faturamento(valores_faturamento)
    maior = maior_faturamento(valores_faturamento)
    media = media_faturamento(valores_faturamento)
    lista_informacoes = {"maiores_faturamentos": [], "menores_faturamentos": [], "acima_media_faturamento": []}

    with open("dados.json") as arquivo_dados:
        faturamento = json.load(arquivo_dados)
        for informacao in faturamento:
            if informacao["valor"] == maior:
                lista_informacoes["maiores_faturamentos"].append(informacao)
            if informacao["valor"] == menor:
                lista_informacoes["menores_faturamentos"].append(informacao)
            if informacao["valor"] > media:
                lista_informacoes["acima_media_faturamento"].append(informacao)
    
    return lista_informacoes


def imprimir_informacoes():
    lista_informacoes = informacoes_faturamento()
    print('\n=================================================\n INFORMACOES SOBRE O FATURAMENTO')
    print('\n\n MENOR FATURAMENTO DO MÊS\n-------------------------------------------------')
    print(f'Quantidade de dias com o menor faturamento: {len(lista_informacoes["menores_faturamentos"])}\n')

    for informacao in lista_informacoes["menores_faturamentos"]:
        print(f'Dia: {informacao["dia"]: >2} | Valor: {informacao["valor"]: >.2f}')
    
    print('\n\n MAIOR FATURAMENTO DO MÊS\n-------------------------------------------------')
    print(f'Quantidade de dias com o maior faturamento: {len(lista_informacoes["maiores_faturamentos"])}\n')
    for informacao in lista_informacoes["maiores_faturamentos"]:
        print(f'Dia: {informacao["dia"]: >2} | Valor: {informacao["valor"]: >.2f}')
    

    print('\n\n DIAS ACIMA DA MEDIA MENSAL DE FATURAMENTO\n-------------------------------------------------')
    print(f'Valor da media: {media:.2f} | Quantidade de dias acima da media: {len(lista_informacoes["acima_media_faturamento"])}\n')
    for informacao in lista_informacoes["acima_media_faturamento"]:
        print(f'Dia: {informacao["dia"]: >2} | Valor: {informacao["valor"]: >.2f}')
    


imprimir_informacoes()