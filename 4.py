"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""

dados = [
  "SP – R$67.836,43",
  "RJ – R$36.678,66",
  "MG – R$29.229,88",
  "ES – R$27.165,48",
  "Outros – R$19.849,53"
]

faturamento = {}

for dado in dados:
  estado, valor = dado.split(' – ')  # removendo o traço e separando o estado do valor
  valor = float(valor.replace('R$', '').replace('.', '').replace(',', '.'))  # removendo o R$, substituindo a vírgula por ponto e convertendo para float
  faturamento[estado] = valor  # adicionando o estado e o valor ao dicionário

print('Faturamento: ', faturamento)  # checando se o dicionário foi preenchido corretamente

total = sum(faturamento.values())  # somando os valores do dicionário

def percentual(estado, total):  # função para calcular o percentual de representação de cada estado
  return (estado / total) * 100

print('Percentual de representação de cada estado:')
for estado, valor in faturamento.items():
  print(f'{estado}: {percentual(valor, total):.2f}%')  # exibindo o percentual de representação de cada estado
