"""
 Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverter_string(string):
  string_invertida = ''
  for i in range(len(string) - 1, -1, -1):
    # ordem do range:
    #   start (len(string)-1 = index do último caractere),
    #   stop (-1 = faz com que o caractere no index 0 seja incluído),
    #   step (-1 = ir de trás para frente)
    string_invertida += string[i]  # concatenando os caracteres da string invertida
  return string_invertida


string = 'Target, aprova o Wagner!'
print(f'String original: {string}')
print(f'String invertida: {inverter_string(string)}')
