import sqlite3


class ConSqlite():

    @staticmethod
    def getConexao():

        dbName = 'data/RegistroDB'
        conn = sqlite3.connect(dbName +'.sqlite')
        
        return conn
    @staticmethod
    def getDB():
        conn = ConSqlite.getConexao()
        cur = conn.cursor()

        return cur,conn
'''
def AtualizarRegistro(self,codigoCli, nome, CPF, endereco, email, telefone):
        RegistroDAO = RegistroDAO()
        RegistroDAO.Nome = nome
        RegistroDAO.CPF = CPF
        RegistroDAO.Endereco = endereco
        RegistroDAO.Email = email
        RegistroDAO.Telefone = telefone

                
        RegistroDAO.AtualizarRegistro(codigoCli, RegistroDAO)

    def PesquisarTodosRegistros(self):
            RegistroDAO = RegistroDAO()
            query = RegistroDAO.PesquisarTodosRegistros()

            return query

    def PesquisarRegistro(self,valor, tipo):
            RegistroDAO = RegistroDAO()
            query = RegistroDAO.PesquisarRegistro(valor, tipo)

            return query

    def ExcluirRegistro(self,codigoCli):
            RegistroDAO = RegistroDAO()
            RegistroDAO.ExcluirRegistro(codigoCli)
'''


