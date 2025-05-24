# importando SQLite
import sqlite3 as lite
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print('Erro ao concectar com o banco de dados:', e)


# Tabela de cursos --------------

# Criar cursos (Inserir)

def criar_curso(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)'
        cur.execute(query,i)

#criar_curso(['Python', 'Semanas', 50])

# Ver todos os cursos (Selecionar R) CRUD

def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

print(ver_cursos())

#Atualizar os Cursos (Update U) CRUD

def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?'
        cur.execute(query,i)

l = ['Python', 'Duas Semanas', 50.0, 1]
#atualizar_curso(l)

# Deletar os Cursos (Delete D) CRUD

def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)

#deletar_curso([l])

# Tabela de Turmas --------------

# Criar turmas (Inserir)

def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, cursos_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query,i)

# Ver todas as turmas (Read R)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar as Turmas (Update U)

def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Turma SET nome =?, data_inicio=? WHERE id=?'
        cur.execute(query,i)

# Deletar as Turmas (Delete D)

def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Turmas WHERE id=?'
        cur.execute(query,i)

# Tabela de Alunos----------------

# Criar Alunos (Inserir)

def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Ver Alunos (Read R)

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista 

# Atualizar Alunos (Update U)

def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turma SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query,i)

# Deletar Alunos (Delete D)

def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query,i)













    























