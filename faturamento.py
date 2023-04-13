import pandas as pd

# Lendo os dados

dados = pd.read_json('data/dados.json')

# Vendo os dados
# print(dados)
# print(dados.info())


def calcular_valor_min() -> float:

    # Usando pandas poderíamos retornar facilmente com dados.valor.min(), mas vou calcular
    # Como o valor finais de semana e feriados foram pedidos para serem removidos somente da média, não trabalhei com eles aqui

    result = float('inf')

    for number in dados.valor:
        if number < result:
            result = number

    return result


def calcular_valor_max() -> float:

    # Usando pandas poderíamos retornar facilmente com dados.valor.max(), mas vou calcular

    result = float('-inf')

    for number in dados.valor:
        if number > result:
            result = number

    return result

def calcula_media_mes() -> float:

    # Vou calcular também, mas temos funções no pandas para tal

    # Com base no padrão dos dados, no fato de não termos os dias da semana e de como foi escrita a questão, vou considerar todos os zeros como finais de semana e feriados e somente eles

    soma = 0

    for valor in dados.valor:
        if valor != 0:
            soma += valor

    return soma/len(dados.valor)

def verifica_dias_maiores_media() -> int:
    result = 0

    media = calcula_media_mes()

    for valor in dados.valor:
        if valor > media:
            result += 1

    return result

def calcula_percentual() -> dict:
    dados_adicionais = {
        'SP': [67_836.43],
        'RJ': [36_678.66],
        'MG': [29_229.88],
        'ES': [27_165.48],
        'Outros': [19_849.53]
    }

    total = sum([v[0] for v in dados_adicionais.values()])

    for estado in dados_adicionais.keys():
        dados_adicionais[estado].append(dados_adicionais[estado][0]/total)

    return dados_adicionais

print('Questão 03: ')
print('Máximo:', calcular_valor_max())
print('Mínimo:', calcular_valor_min())
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:', verifica_dias_maiores_media())
print()
print('Questão 04:\nPorcentagem dos estados')
for key, value in calcula_percentual().items():
    print(key, f"{value[1]*100:,.2f}%")