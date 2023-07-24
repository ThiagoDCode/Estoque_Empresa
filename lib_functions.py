import connect_banco as ON
import os


def insert_register():
    os.system('cls')

    description = input('Descrição do item: ')
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
    VALUES ('{description}', '{serial}', {quantity}, {price})
    """

    ON.query(ON.conexao_on, tab_sql)


def consult_for(identity=False):
    os.system('cls')
    
    if identity:
        description = input('Descrição ou Serial do Item: ')
        
        tab_sql = f'''
        SELECT * FROM tb_estoque 
            WHERE item_identity LIKE "%{description}%" 
            OR serial_item LIKE "%{description}%"'''
        response = ON.query_select(ON.conexao_on, tab_sql)
    else:
        tb_sql = 'SELECT * FROM tb_estoque'
        response = ON.query_select(ON.conexao_on, tb_sql)

    limit = 5
    for cont, resp in enumerate(response):
        print('=' * 60)
        print(f'|{resp[0]:>5}| {resp[1]:<30} Serial N°: {resp[2]:<9}|')
        print('-' * 60)
        print(f'Quantidade: {resp[3]:<4} Preço: R${resp[4]:<4.2f} \n')
        
        cont += 1
        if cont >= limit:
            cont = 0
            os.system('pause')
            os.system('cls')
    print(' SEM MAIS RESULTADOS... '.center(60, '-'))
    print()
    os.system('pause')


def update_register():
    os.system('cls')

    id = input('ID do registro a ser alterado: ')
    result = ON.query_select(ON.conexao_on, 'SELECT *FROM tb_estoque WHERE ID_item='+id)
    r_item = result[0][1]
    r_serial = result[0][2]
    r_quantity = result[0][3]
    r_price = result[0][4]

    item = input('Descrição do item: ')
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

    ON.query(ON.conexao_on, tb_sql)


def delete_register():
    os.system('cls')

    id = input('ID do registro a ser deletado: ')
    tb_sql = f'DELETE FROM tb_estoque WHERE ID_item={id}'

    ON.query(ON.conexao_on, tb_sql)
