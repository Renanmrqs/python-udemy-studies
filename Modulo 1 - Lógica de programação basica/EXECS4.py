"""
Exercicio 1:

Faça um programa que peça ao usúario para digitar um número inteiro,
Informe se este número é par ou ímpar. Caso o usúario não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Exercicio 2:

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Exercicio 3:

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# numero = input('escreva um numero inteiro: ')

# try:
#     numero_int = int(numero)     
#     if (numero_int % 2 == 0):
#         print(f'{numero} é par')
#     else:
#      print(f'{numero} é impar')
# except:
#     print('Não é um número inteiro')

# CODIGO DO PROFESSOR -> entrada = input('Digite um numero inteiro: ')

# if entrada.isdigit():
#    entrada_int = int(entrada)
#    par_impar = entrada_int % 2 == 0 
#    par_impar_texto = 'impar'

# if par_impar:
#     par_impar_texto = 'par'
#     print(f'o numero {entrada_int} é {par_impar_texto}')
# else:
#     print('voce nao digitou um numero intero')
   

# CODIGO DO PROFESSOR -> entrada = input('Digite a hora em numero inteiro: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia parceiro!')
#     elif hora >= 12 and hora <= 17:  
#         print('Boa tarde parceiro!')
#     elif hora >= 18 and  hora <= 23:
#         print('Boa noite parceiro!')
#     else:
#         print('não conheço essa hora')

# except:
#     print('digite apenas numeros inteiros por favor!')

# horario = input('Fala parceiro! que horas são?')
# horario_int = int(horario)

# if horario_int >= 0 or horario_int <= 11:
#    print('Bom dia parceiro!')
# elif horario_int >= 12 or horario_int <= 17:
#     print('Boa tarde parceiro!')
# elif horario_int <= 18 or horario_int >= 23:
#     print('Boa noite parceiro!')

# primeiro_nome = input('Qual seu primeiro nome?')
# check_name = len(primeiro_nome)

# if check_name <= 4:
#     print('seu nome é curto')
# elif check_name == 5 and check_name == 6:
#     print('seu nome e normal')
# else check_name >= 6:
#     print('seu nome e grande')

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('seu nome e medio')
    else:
        print('seu nome e mt grande')
else:
    print('digite ao menos uma letra porfavo')


    
