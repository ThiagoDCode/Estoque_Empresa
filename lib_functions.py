import connect_banco as con
import os


def insert_register():
    os.system('cls')

    identity = input('Identificação do item: ')
    serial = input('Número serial do item: ')
    quantity = int(input('Quantidade para registro: '))
    price = float(input('Preço do item: R$'))

    tab_sql = f"""
    INSERT INTO tb_estoque (
        item_identity,
        serial_item,
        quantity,
        price_unit
    )
    VALUES ('{identity}', '{serial}', {quantity}, {price})
    """

    con.query(con.conexao_on, tab_sql)


def consult_register():
    os.system('cls')

    tb_sql = 'SELECT * FROM tb_estoque'
    result = con.query_select(con.conexao_on, tb_sql)

    limit = 10
    cont = 0
    for search in result:
        print(f'ID: {search[0]:<3} Item: {search[1]:.<30} Serial: {search[2]:<9} Quantidade: {search[3]:<4} Preço: R${search[4]:<4}')
        cont += 1
        if cont >= limit:
            cont = 0
            os.system('pause')
            os.system('cls')
    print(' SEM MAIS RESULTADOS '.center(50, '-'))
    print()
    os.system('pause')


def consult_for_ident():
    os.system('cls')

    identity = input('Identificação do Item: ')
    tab_sql = 'SELECT * FROM tb_estoque WHERE item_identity LIKE "%'+identity+'%"'
    result = con.query_select(con.conexao_on, tab_sql)

    limit = 5
    cont = 0
    for search in result:
        print(f'ID: {search[0]:<3} Item: {search[1]:.<30} Serial: {search[2]:<9} Quantidade: {search[3]:<4} Preço: R${search[4]:<4}')
        cont += 1
        if cont >= limit:
            cont = 0
            os.system('pause')
            os.system('cls')
    print(' SEM MAIS RESULTADOS '.center(50, '-'))
    print()
    os.system('pause')


def update_register():
    os.system('cls')

    id = input('ID do registro a ser alterado: ')
    result = con.query_select(con.conexao_on, 'SELECT *FROM tb_estoque WHERE ID_item='+id)
    r_item = result[0][1]
    r_serial = result[0][2]
    r_quantity = result[0][3]
    r_price = result[0][4]

    item = input('Identificação do item: ')
    serial = input('Serial do item: ')
    quantity = input('Quantidade para registro: ')
    price = input('Preço do item: ')

    if len(item) == 0:
        item = r_item
    if len(serial) == 0:
        serial = r_serial
    if len(str(quantity)) == 0:
        quantity = r_quantity
    if len(str(price)) == 0:
        price = r_price

    tb_sql = f"""
    UPDATE tb_estoque SET
        item_identity='{item}',
        serial_item='{serial}',
        quantity='{int(quantity)}',
        price_unit='{float(price)}'
    WHERE ID_item={id}
    """

    con.query(con.conexao_on, tb_sql)


def delete_register():
    os.system('cls')

    id = input('ID do registro a ser deletado: ')
    tb_sql = f'DELETE FROM tb_estoque WHERE ID_item={id}'

    con.query(con.conexao_on, tb_sql)
