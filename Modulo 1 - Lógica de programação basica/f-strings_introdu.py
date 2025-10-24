nome = 'Renan Marques'
altura = 1.70
peso = 69
IMC = peso / (altura * altura)
 
"f-strings" 
linha1 = f'{nome} tem {altura:.1f} de altura'
linha2 = f'pesa {peso} quilos e seu IMC é:'
linha3 = f'{IMC:.2f}'

print(linha1)
print(linha2)
print(linha3)