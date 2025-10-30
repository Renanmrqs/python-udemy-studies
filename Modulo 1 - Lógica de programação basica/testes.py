
# import sqlite3

# # 2. Conectar-se ao banco de dados (se não existir, ele cria)
# conn = sqlite3.connect('serie_b.db')
# cursor = conn.cursor()

# # 3. Executar um comando SQL para criar uma tabela
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS times (
#         id INTEGER PRIMARY KEY,
#         nome TEXT NOT NULL,
#         pontos INTEGER
#     )
# ''')

# # 4. Inserir um novo time
# cursor.execute("INSERT INTO times (nome, pontos) VALUES (?, ?)", ('Vasco', 40), )

# # 5. Salvar as mudanças
# conn.commit()

# # 6. Fechar a conexão
# conn.close()

# print("Tabela criada e time inserido com sucesso!")

"""

Exercicio
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
    exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contem(ou nao) espaços
        Seu nome tem {n} letras
        A primeira letra de seu nome é {letra}
        A ultima letra do seu nome é {Letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios"
"""
# nome = input('Digite seu nome: ')    
# idade = input('Digite sua idade: ')
# #int_idade = int(idade)
# nome_inver = (nome[-1::-1])
# quantidade = (len(nome))

# if nome and idade == '':
#     print('Desculpe, voce deixou campos vazios')
# elif nome in nome:
#     print (f'seu nome: {nome}')
#     print (f'seu nome invertido: {nome_inver}')
#     print(f'seu nome tem: {quantidade} letras')
#     print(f'a primeira letra do seu nome é {nome[0]}') #renan
#     print(f'a ultima letra do seu nome é: {nome[-1]}')

# if (' ' in nome):
#     print('seu nome contem espaço')
# else:
#     print('seu nome nao contem espaço')

nome = input('Digite seu nome: ')    
idade = input('Digite sua idade: ')

if nome and idade:
    print (f'seu nome: {nome}')
    print (f'seu nome invertido: {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contem  espaços')
    else:
        print('Seu nome NAO contem  espaços')

    print(F'Seu nome tem: {len(nome)} letras')
    print(F'A primeira leta do seu nome é: {nome[0]}')
    print(F'A Ultima leta do seu nome é: {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')