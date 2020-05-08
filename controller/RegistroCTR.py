
from os import getcwd
from sys import path, platform
path.extend(['/'.join(getcwd().split('/')[0:-4])])

from model.DAO.RegistroDAO import RegistroDAO
from model.DMO.RegistroDMO import RegistroDMO


class RegistroCTR():

        def CadastrarRegistro(self,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida):

            DAO = RegistroDAO()

            DAO.Laboratorio = Laboratorio
            DAO.NumeroPatri = NumeroPatri
            DAO.NumeroSerie = NumeroSerie
            DAO.Padrao = Padrao
            DAO.Modelo = Modelo
            DAO.Fabricante = Fabricante
            DAO.DataCali = DataCali
            DAO.DataChec = DataChec
            DAO.DataVenc = DataVenc
            DAO.DataProxCali = DataProxCali
            DAO.DataSaida = DataSaida
        
            DMO = RegistroDMO()
            DMO.CadastrarRegistro(DAO)


        def AtualizarRegistro(self,IDReg,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida):

                DAO = RegistroDAO()

                DAO.Laboratorio = Laboratorio
                DAO.NumeroPatri = NumeroPatri
                DAO.NumeroSerie = NumeroSerie
                DAO.Padrao = Padrao
                DAO.Modelo = Modelo
                DAO.Fabricante = Fabricante
                DAO.DataCali = DataCali
                DAO.DataChec = DataChec
                DAO.DataVenc = DataVenc
                DAO.DataProxCali = DataProxCali
                DAO.DataSaida = DataSaida
                DMO = RegistroDMO()
                DMO.AtualizarRegistro(IDReg,DAO)

        def PesquisarTodosRegistros(self):
                DMO = RegistroDMO()
                query = DMO.PesquisarTodosRegistros()

                return query

        def PesquisarRegistro(self,tipo, valor):
                DMO = RegistroDMO()
                query = DMO.PesquisarRegistro(tipo,valor)

                return query

        def ExcluirRegistro(self,IDReg):
                DMO = RegistroDMO()
                DMO.ExcluirRegistro(IDReg)






'''
e = ExcluirRegistro('4')
'''

'''
p = PesquisarRegistro('ID','2')
print(p)
'''

'''
d = PesquisarTodosRegistro()
print(d)
'''

'''
bla = RegistroCTR()
bla.CadastrarRegistro('UA30',
'7747453533',
'36961355552121',
'Osciloscópio',
'Fluke Sa20',
'Fluke',
'27/04/2020',
'20/04/2020',
'27/04/2021',
'27/04/2021',
'21/04/2021')
'''