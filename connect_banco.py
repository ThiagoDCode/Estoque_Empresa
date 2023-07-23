import os
import sqlite3
from sqlite3 import Error
from time import sleep


# Conexão com o Banco
def connect_banco():
    caminho = 'db_estoque\\estoque.db'
    conexao = None

    try:
        conexao = sqlite3.connect(caminho)
        os.system('cls')
        print('\nConexão Estabelecida! \n')
        sleep(1.5)
    except Error as erro:
        print(erro)

    return conexao


conexao_on = connect_banco()


# QUERY para instruções: INSERT / UPDATE / DELETE
def query(conexao, sql):
    try:
        connect = conexao.cursor()
        connect.execute(sql)
        conexao.commit()
    except Error as erro:
        print(erro)
        os.system('pause')
    else:
        print('Registro realizado com sucesso!')
        sleep(1.5)


# QUERY para instrução: SELECT
def query_select(conexao, sql):
    connect = conexao.cursor()
    connect.execute(sql)
    resposta = connect.fetchall()

    return resposta
