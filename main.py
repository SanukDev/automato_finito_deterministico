# Automato finito
# Atividade A1
# Samuel Rodrigues Melo
# RGM: 32765185
# Problema 8 Cadeias de comprimento múltiplo de 3.

# ----------------- Regras de produção:

# ∑ = {a,b,c}
# S = XXXS
# X = a
# X = b
# X = c
# S = ε
# ((a|b|c)(a|b|c)(a|b|c))*


final = True
def problema8(cadeia):
    cadeia = cadeia
    # Analisa os caracteres possíveis dentro da cadeia.
    conjunto = ['a','b','c']
    cont = 0
    for i in cadeia:
      if i not in conjunto:
          cont = 1
    # Verifica o tamanho da cadeia considerando o resto; caso satisfaça a condição, a cadeia é aceita.
    if cont == 1:
      print('cadeia nao aceita')
    elif len(cadeia) % 3 != 0:
      print('cadeia nao aceita')
    else:
      print('cadeia aceita')

while final:
  cadeia = input('Digite uma cadeia de caracteres de comprimento múltiplo de 3, dos conjuntos possiveis do alfabeto ["a","b","c"]: ')
  problema8(cadeia)
  var = input('Deseja continuar? [s/n]: ')
  if var.lower() == 'n':
    final = False
