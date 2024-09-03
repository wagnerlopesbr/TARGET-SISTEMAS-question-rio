"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json


with open('dados.json', 'r') as file:  # lendo o arquivo json
  dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]  # pegando os valores maiores que 0 para ignorar os dias sem faturamento

menor = min(valores)
maior = max(valores)

media = sum(valores) / len(valores)

dias_acima_media = len([valor for valor in valores if valor > media])  # pegando os valores maiores que a média

print(f'Menor valor de faturamento: {menor}')
print(f'Maior valor de faturamento: {maior}')
print(f'Número de dias com faturamento acima da média: {dias_acima_media}')
