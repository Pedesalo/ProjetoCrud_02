import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="locahost",
            user="root",
            password="root",
            database="claus_db"
        )
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuario(id_usuario INT AUTO INCREMENT PRIMARY KEY,
                          nome VARCHAR(40),
                          telefone VARCHAR(16),
                          email VARCHAR(40), 
                          usuario VARCHAR(40), 
                          senha VARCHAR(40))''')
        
        self.conexao.commit()
        c.close()