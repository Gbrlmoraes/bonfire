# Tratamento de dados
import pandas as pd

# Conexão com o banco SQL
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import urllib

# Auxiliares
import time

# Função para fazer a conexão com o banco SQL
def conecta_sql(host  : str, login : str, database : str, senha : str, fast_executemany : bool = False):
    '''
    Descrição:
    - Função para fazer a conexão com o banco
    ===
    Argumentos:
    host (str) : host do banco de dados
    login (str) : login do banco de dados
    senha (str) : senha do banco de dados
    fast_executemany (bool, opcional) : guarda todos os valores na memória de uma vez e depois sobe todos para o banco, esse
    método aumenta a velocidade de carregamento dos dados, mas deve ser usado com cuidado dependendo do volume de dados
    ===
    Retorno:
    - Objeto SQLAlchemy de conexão com o banco de dados
    '''
    driver = '{ODBC Driver 18 for SQL Server}'
    odbc_str = f'DRIVER={driver};SERVER={host};PORT=1433;UID={login};DATABASE={database};PWD={senha}'
    string_conexao = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)            

    try:
        engine = create_engine(string_conexao, fast_executemany = fast_executemany)

        conexao = engine.connect()
        print('Conexão OK!')

        return conexao

    except SQLAlchemyError as e:
        print('Ocorreu um erro na conexão!')
        print(e)
       
# Função para fazer o upload dos dados para o banco SQL
def envia_sql(conexao : any, dataframe : pd.DataFrame, nome_tabela : str, schema : str):
    '''
    Descrição:
    - Função para fazer o carregamento dos dados para o banco de dados
    Argumentos:
    - conexao : Objeto de conexão do SQLAlchemy
    - schema : Schema onde ficarão as tabelas no banco
    - dataframe : Dataframe pandas com os dados
    - nome_tabela : Nome que a tabela terá no banco de dados
    '''
    try:
        tic = time.time()
        print(f'Subindo tabela: {nome_tabela} para o banco SQL')
        dataframe.to_sql(
            nome_tabela,
            con = conexao,
            schema = schema,
            index = False,
            if_exists = 'replace'
        )
        toc = time.time()
        print(f'Tabela enviada!. Tempo de envio: {(toc - tic) / 60:.2f} min')

    except Exception as e:
        print(f'Falha ao enviar a tabela: {nome_tabela}')
        print(str(e))