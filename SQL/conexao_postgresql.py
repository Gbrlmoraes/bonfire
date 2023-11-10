# Imports necessários
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Função para se conectar com o banco de dados
def conecta_postgres(host: str, usuario: str, database: str, senha: str):
    '''
    Descrição:
    - Função para fazer a conexão com o banco
    ===
    Argumentos:
    host (str) : host do banco de dados
    login (str) : login do banco de dados
    senha (str) : senha do banco de dados
    ===
    Retorno:
    - Objeto SQLAlchemy de conexão com o banco de dados
    '''
    # String de conexão para o PostgreSQL
    conn_str = f"postgresql://{usuario}:{senha}@{host}/{database}"

    try:
        engine = create_engine(conn_str)

        conexao = engine.connect()
        print('Conexão OK!')

        return conexao

    except SQLAlchemyError as e:
        print('Ocorreu um erro na conexão!')
        print(e)
       
# Função para fazer o upload dos dados para o banco SQL
def envia_sql(conexao : any, dataframe : pd.DataFrame, nome_tabela : str, schema : str = 'public', if_exists : str = 'replace'):
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
        dataframe.to_sql(
            nome_tabela,
            con = conexao,
            schema = schema,
            index = False,
            if_exists = if_exists
        )
    except Exception as e:
        print(f'Falha ao enviar a tabela: {nome_tabela}')
        print(str(e))