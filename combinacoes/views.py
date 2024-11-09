import os
from django.shortcuts import render
import csv
import random
import pandas as pd
import math
from typing import List, Dict, Tuple

# Caminho do arquivo CSV na raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'lotofacilatual1.csv')

# Função para gerar combinações com base nas dezenas mais sorteadas
def gerar_combinacoes(dezenas: List[int], total_dezenas: int, num_combinacoes: int) -> List[List[int]]:
    combinacoes = set()
    while len(combinacoes) < num_combinacoes:
        combinacao = sorted(random.sample(dezenas, total_dezenas))
        combinacoes.add(tuple(combinacao))  # Convertendo para tuple para poder adicionar ao set
    return [list(comb) for comb in combinacoes]

# Função para calcular a probabilidade de uma combinação acertar um determinado número de dezenas
def calcular_probabilidade(dezenas: int, total_dezenas: int, acertos: int) -> float:
    if dezenas == acertos and dezenas == total_dezenas:
        return 1.0  # Se todas as dezenas foram escolhidas, a probabilidade de acertar todas é 100%
    
    combinacoes_possiveis = math.comb(dezenas, acertos)
    total_combinacoes = math.comb(total_dezenas, acertos)

    return combinacoes_possiveis / total_combinacoes

# Função para contar as vezes que a combinação foi sorteada com 12, 13, 14 ou 15 dezenas
def contar_sorteios(comb: List[int], resultados: List[str]) -> Dict[int, int]:
    contagem = {12: 0, 13: 0, 14: 0, 15: 0}
    for resultado in resultados:
        numeros_sorteados = set(map(int, resultado.split(",")))
        acertos_comb = len(set(comb).intersection(numeros_sorteados))
        if acertos_comb >= 12:
            contagem[acertos_comb] += 1
    return contagem

# Função para verificar se um número é primo
def is_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Função para contar pares, ímpares, números primos e repetições
def contar_caracteristicas(comb: List[int]) -> Tuple[int, int, int, int]:
    pares = sum(1 for x in comb if x % 2 == 0)
    impares = sum(1 for x in comb if x % 2 != 0)
    primos = sum(1 for x in comb if is_primo(x))
    repeticoes = len(comb) - len(set(comb))
    return pares, impares, primos, repeticoes

# View principal para gerar combinações e exibir os melhores resultados
def gerar_combinacoes_view(request):
    # Carrega os resultados do arquivo CSV
    resultados = []
    with open(CSV_PATH, 'r') as arquivo:
        linhas = csv.reader(arquivo)
        for linha in linhas:
            resultados.append(",".join(linha))

    # Defina as variáveis necessárias
    total_dezenas = 15
    num_combinacoes = 10000
    dezenas_mais_sorteadas = list(range(1, 26))

    # Gere as combinações e compile os dados para o DataFrame
    data = []
    for i, combinacao in enumerate(gerar_combinacoes(dezenas_mais_sorteadas, total_dezenas, num_combinacoes), start=1):
        prob_15 = calcular_probabilidade(total_dezenas, 25, 15)
        contagem = contar_sorteios(combinacao, resultados)
        pares, impares, primos, repeticoes = contar_caracteristicas(combinacao)
        data.append({
            "id": i,
            "combinação": combinacao,
            "probabilidade_15_acertos": prob_15,
            "12_acertos": contagem[12],
            "13_acertos": contagem[13],
            "14_acertos": contagem[14],
            "15_acertos": contagem[15],
            "pares": pares,
            "ímpares": impares,
            "primos": primos,
            "repetições": repeticoes
        })

    # Converte os dados para um DataFrame
    df = pd.DataFrame(data)

    # Seleciona as 5 melhores combinações para cada faixa de acertos
    melhores_combinacoes = {
        12: df.nlargest(5, '12_acertos').to_dict('records'),
        13: df.nlargest(5, '13_acertos').to_dict('records'),
        14: df.nlargest(5, '14_acertos').to_dict('records'),
        15: df.nlargest(5, '15_acertos').to_dict('records')
    }

    # Renderiza a página com os melhores dados
    return render(request, 'combinacoes/resultado.html', {"melhores_combinacoes": melhores_combinacoes})
