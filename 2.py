"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

def fibonacci(n):
  fib1, fib2 = 0, 1  # trabalharei com tuplas para atualizar os valores da sequência
  if n == fib1 or n == fib2:  # verifica se n é 0 ou 1
    return True
  
  while fib2 < n:  # enquanto o próximo valor da sequência for menor que n
    fib1, fib2 = fib2, fib1 + fib2  # atualiza os valores da sequência

  return n == fib2  # verifica se n é igual ao próximo valor da sequência


n = 21  # retorna o if, pois 21 pertence a sequência de Fibonacci

if fibonacci(n):
  print(f'{n} pertence a sequência de Fibonacci')
else:
  print(f'{n} não pertence a sequência de Fibonacci')


n = 22  # retorna o else, pois 22 pertence a sequência de Fibonacci

if fibonacci(n):
  print(f'{n} pertence a sequência de Fibonacci')
else:
  print(f'{n} não pertence a sequência de Fibonacci')


n = 34  # retorna o if, pois 34 pertence a sequência de Fibonacci

if fibonacci(n):
  print(f'{n} pertence a sequência de Fibonacci')
else:
  print(f'{n} não pertence a sequência de Fibonacci')
