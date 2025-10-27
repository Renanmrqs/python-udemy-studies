
import sqlite3

# 2. Conectar-se ao banco de dados (se não existir, ele cria)
conn = sqlite3.connect('serie_b.db')
cursor = conn.cursor()

# 3. Executar um comando SQL para criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        pontos INTEGER
    )
''')

# 4. Inserir um novo time
cursor.execute("INSERT INTO times (nome, pontos) VALUES (?, ?)", ('Vasco', 40), )

# 5. Salvar as mudanças
conn.commit()

# 6. Fechar a conexão
conn.close()

print("Tabela criada e time inserido com sucesso!")