import sqlite3
import pandas as pd
import os


class CertificadoCTR:


    def __init__(self,PATH_NAME,banco_cert):

        self.PATH_NAME = PATH_NAME
        self.banco_cert = banco_cert

    def dicio(self):

        #varrendo todos os arquivos com extensao xlsxda pasta de registro
        todos_arquivos = list(filter(lambda x:'.xlsx' in x,os.listdir(self.PATH_NAME)))
        todos_dataset = []
        d = {}
        campos_tabela = []

        #varrendo os arquivos e inserindo no dicionario
        for arquivos in todos_arquivos:
            data = pd.read_excel(self.PATH_NAME + arquivos,sheet_name = None ,header = 0)
            todos_dataset.append(data)
            campos_tabela.append(list(data.keys()))
            
        #conectando com o banco de dados
        conn = sqlite3.connect(self.banco_cert +'.sqlite')

        #obtendo nome das tabelas xlsx
        nome_tabela = [os.path.splitext(i)[0] for i in todos_arquivos]
    
        #Apenas para teste, excluir depois
        cur = conn.cursor()
        for b in range(0,len(nome_tabela)):
            cur.execute('DROP TABLE IF EXISTS '+nome_tabela[b])
    
    
        nomeHeader = []
        i= 0
        k=0

        #obtendo o cabeçalho de cada aba da planilha
        for i in range (0,len(todos_dataset)):
            for k in range(0,len(campos_tabela[i])):
                nomeHeader.append(list(todos_dataset[i][campos_tabela[i][k]].keys()))


        #print(nomeHeader)
        #for j in range(0,len(nome_tabela)):
        #print(str(campos_tabela[j].items()))
        
        print('\nNome das Tabelas\n')
        print(nome_tabela)
        print('\nNome das abas das Tabelas')
        print(campos_tabela)
        print('\nNome das colunas de cada aba')
        print(nomeHeader)


        j=0
        for j in range(0,len(nome_tabela)):
            cur.execute("""CREATE TABLE IF NOT EXISTS """+nome_tabela[j]+"""("""+','.join(campos_tabela[j])+""")""")


        k=0
        i=0
        for index in range(0,len(nome_tabela)):
                query = """INSERT INTO """+str(nome_tabela[index])+"""("""+','.join(campos_tabela[index])+""")VALUES("""+','.join(map(str,'?'*len(pd.DataFrame([todos_dataset[index]]).columns)))+""")"""
                todos_dataset[index] = pd.DataFrame([todos_dataset[index]]).astype(str)
                #print('Separando Todos_dataset\n\n')
                #print(todos_dataset[index])
                #
                for k in range(0,len(todos_dataset[index])):
                    
                    inserir_registro = tuple(todos_dataset[index].iloc[k])
                    cur.execute(query,inserir_registro)
                    conn.commit()