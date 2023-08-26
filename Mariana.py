import sqlite3

class Aluno:
    def __init__(self,id,nome):
        self.id = id,
        self.nome = nome

def lista_todos():
    cursor.execute ("select * from ALUNO")
    c = cursor.fetchall()

    for item in c:
        print(item)


def altera_aluno(aluno:Aluno):
    cursor.execute(f"UPDATE aluno SET nome = ? where id=?",(aluno.nome,aluno.id))

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE aluno 
#                (id integer primary key autoincrement,
#               nome varchar(30) not null )""")

sql = """INSERT INTO ALUNO (nome) values ('MARIANA');
         INSERT INTO ALUNO (nome) values ('MARCUS');"""
cursor.executescript(sql)

lista_todos()



idAluno = input("Qual ID deseja alterar ?")    
novoNome = input("Informe o novo nome")

aluno = Aluno(idAluno,novoNome)

altera_aluno(aluno)

lista_todos()

conn.commit()
cursor.close()
conn.close()


