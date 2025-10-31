"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdaeira
\
"""



# while True:
#    nome = input('qual seu nome: ')
#    print(f'Seu nome é {nome}, mentira ne?  ')

#    if nome == nome:
#     break
   
# print('acabouse')

contador = 0

while contador <= 100: #contador basico do 1 ao 10
    contador += 1
    
    if contador == 6:
        print('nao vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 20:
        print('nao vou mostrar o', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break



  
    
    
   
    


    
    


