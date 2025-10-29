"""
Formatação básica de strings
s - string
d - int
f - float
. <número de dígitos> f
x ou X - Hexadecimal
(Caractere) (><^) (Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex. 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >15}')
print(f'{variavel: <15}.')
print(f'{variavel: ^15}.')
print(f'{1000.4565354656:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
