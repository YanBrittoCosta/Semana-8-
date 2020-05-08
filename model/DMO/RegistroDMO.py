from PyQt5.QtSql import QSqlQuery
import sqlite3

from os import getcwd
from sys import path, platform
path.extend(['/'.join(getcwd().split('/')[0:-4])])

from data.ConSqlite import ConSqlite
from model.DAO.RegistroDAO import RegistroDAO

class RegistroDMO():

    def CriarTabela(self):
        
        cur,conn = ConSqlite.getDB()

        tab = cur.execute('''CREATE TABLE IF NOT EXISTS Registro(
                    IDReg  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    Laboratorio TEXT,
                    NumeroPatri INTEGER UNIQUE,
                    NumeroSerie INTEGER UNIQUE,
                    Padrao TEXT,
                    Modelo TEXT,
                    Fabricante TEXT,
                    DataCali TEXT,
                    DataChec TEXT,
                    DataVenc TEXT,
                    DataProxCali TEXT,
                    DataSaida TEXT)'''
                    )
        conn.commit()
        cur.close()

    def CadastrarRegistro(self,registro):

        cur,conn = ConSqlite.getDB()

        cur.execute('INSERT INTO Registro('
            'Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,DataCali,DataChec,DataVenc,DataProxCali,DataSaida)'
            'VALUES(?,?,?,?,?,?,?,?,?,?,?)',
            (registro.Laboratorio, registro.NumeroPatri, registro.NumeroSerie,registro.Padrao,registro.Modelo,registro.Fabricante,
            registro.DataCali,registro.DataChec,registro.DataVenc,registro.DataProxCali,registro.DataSaida,)
            )

        conn.commit()
        cur.close()


    def AtualizarRegistro(self,IDReg,registro):

        cur,conn = ConSqlite.getDB()


        cur.execute("UPDATE Registro SET Laboratorio = '"+registro.Laboratorio
                    +"',NumeroPatri = '"  +registro.NumeroPatri
                    +"',NumeroSerie = '"  +registro.NumeroSerie
                    +"',Padrao = '"  +registro.Padrao
                    +"',Modelo = '"  +registro.Modelo
                    +"',Fabricante = '"  +registro.Fabricante
                    +"',DataCali = '"  +registro.DataCali
                    +"',DataChec = '"  +registro.DataChec
                    +"',DataVenc = '"  +registro.DataVenc
                    +"',DataProxCali = '"  +registro.DataProxCali
                    +"',DataSaida = '"  +registro.DataSaida
                    +"'WHERE IDReg = " +IDReg)


        conn.commit()
        cur.close()

    

    def PesquisarTodosRegistros(self):

        cur,conn = ConSqlite.getDB()

        query = cur.execute('SELECT * FROM Registro')
        
        return query.fetchall()


    def PesquisarRegistro(self,tipo,valor):

        cur,conn = ConSqlite.getDB()

        if tipo=='ID':
            
                query = cur.execute("SELECT * FROM Registro WHERE IDReg = '"+valor+"'")
                return query.fetchall()
    
        elif tipo=='Padrão':
            query = cur.execute("SELECT * FROM Registro WHERE Padrao = '"+valor+"'")
            return query.fetchall()
                

        elif tipo=='Número de Série':
            query = cur.execute("SELECT * FROM Registro WHERE NumeroSerie = '"+valor+"'")
            return query.fetchall()
        
        elif tipo=='Patrimônio':
            query = cur.execute("SELECT * FROM Registro WHERE NumeroPatri = '"+valor+"'")
            return query.fetchall()


    def ExcluirRegistro(self,IDReg):

        cur,conn = ConSqlite.getDB()

        cur.execute("DELETE FROM Registro WHERE IDReg = '"+IDReg+"'")

        conn.commit()
        cur.close()        


#print(PesquisarTodosRegistros())

#print(PesquisarRegistro('ID','3'))

'''
reg = RegistroDMO()
a = reg.PesquisarRegistro('Patrimônio','1234567')
print(a)
'''

'''
regtesteATT = RegistroDAO()
regtesteATT.Laboratorio = 'CA2'
regtesteATT.NumeroPatri = '000'
regtesteATT.NumeroSerie = '111'
regtesteATT.Padrao = 'Osciloscópio'
regtesteATT.Modelo = 'Fluke Sa20'
regtesteATT.Fabricante = 'Fluke'
regtesteATT.DataCali = '27/04/2020'
regtesteATT.DataChec = '20/04/2020'
regtesteATT.DataVenc = '27/04/2021'
regtesteATT.DataProxCali = '27/04/2021'
regtesteATT.DataSaida = '21/04/2021'
AtualizarRegistro(1,regtesteATT)
'''
#CriarTabela()
'''
regteste = RegistroDAO()
regteste.Laboratorio = 'CA2'
regteste.NumeroPatri = '12345678'
regteste.NumeroSerie = '0987659'
regteste.Padrao = 'Osciloscópio'
regteste.Modelo = 'Fluke Sa20'
regteste.Fabricante = 'Fluke'
regteste.DataCali = '27/04/2020'
regteste.DataChec = '20/04/2020'
regteste.DataVenc = '27/04/2021'
regteste.DataProxCali = '27/04/2021'
regteste.DataSaida = '21/04/2021'
CadastrarRegistro(regteste)
'''







