import extras as EX
import os
import sqlite3
from sqlite3 import Error
from time import sleep


# Conexão com o Banco
def connect_banco():
    caminho = "./estoque_empresa/main/db_estoque/estoque.db"
    #caminho = 'db_estoque\\estoque.db'
    connection = None

    try:
        connection = sqlite3.connect(caminho)
        os.system('cls')
        print('\nConexão Estabelecida! \n')
        sleep(1.5)
    except Error as erro:
        print(EX.error(erro))

    return connection


connection_ON = connect_banco()


# QUERY para instruções: INSERT / UPDATE / DELETE
def query(connection_db, sql):
    try:
        connect = connection_db.cursor()
        connect.execute(sql)
        connection_db.commit()
    except Error as erro:
        print(EX.error(erro))
        os.system('pause')
    else:
        print('\nREGISTRO REALIZADO COM SUCESSO!\n')
        sleep(1.5)


# QUERY para instrução: SELECT
def query_select(connection_db, sql):
    connect = connection_db.cursor()
    connect.execute(sql)
    resposta = connect.fetchall()

    return resposta
