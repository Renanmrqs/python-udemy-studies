# Operadores in e not in
# Strings sao iteraveis
# 0 1 2 3 4 5 6
# R e n a n
# -6-5-4-3-2-1
# nome = 'Renan'
# print('Ren' in nome)
# print('an' in nome)
# print(12 * '-')
# print('Ren' not in nome)
# print('an' not in nome)

nome = input ('Digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
