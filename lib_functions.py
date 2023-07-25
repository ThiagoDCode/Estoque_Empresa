import connect_banco as ON
import os


def insert_register():
    """ Adiciona novo item ao Banco de Dados
    """
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

    ON.query(ON.connection_ON, tab_sql)


def consult_register(identity=False):
    """ Consulta e imprime os dados do Banco de Dados

    Args:
        identity (bool, optional): Se True, habilita a consulta por dados específicos. Defaults to False.
    """
    os.system('cls')
    
    if identity:
        description = input('Descrição ou Serial do Item: ')
        
        tab_sql = f'''
        SELECT * FROM tb_estoque 
            WHERE item_identity LIKE "%{description}%" 
            OR serial_item LIKE "%{description}%"'''
        response = ON.query_select(ON.connection_ON, tab_sql)
    else:
        tb_sql = 'SELECT * FROM tb_estoque'
        response = ON.query_select(ON.connection_ON, tb_sql)

    limit = 5
    for cont, resp in enumerate(response):
        print('=' * 60)
        print(f'|{resp[0]:^3}| {resp[1]:^30} |Serial N°: {resp[2]:^10}|')
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
    
    id = input('Digite o ID do registro a ser alterado: ')
    response = ON.query_select(ON.connection_ON, 'SELECT * FROM tb_estoque WHERE ID_item='+id)

    # PRINT ------------------------------------------------------------------------
    for resp in response:
        dados_item = [resp[0], resp[1], resp[2], resp[3], resp[4]]
        print('=' * 60)
        print(f'|{resp[0]:^3}| {resp[1]:^30} |Serial N°: {resp[2]:^10}|')
        print('-' * 60)
        print(f'Quantidade: {resp[3]:<4} Preço: R${resp[4]:<4.2f} \n')
    # ------------------------------------------------------------------------ PRINT
    
    new_item = input('Alterar descrição do item? ')
    new_serial = input('Alterar serial do item? ')
    new_quantity = input('Alterar quantidade do registro? ')
    new_price = input('Altear preço do item? ')
    
    tab_sql = f"""
    UPDATE tb_estoque SET
        item_identity='{new_item if len(new_item) != 0 else dados_item[1]}',
        serial_item='{new_serial if len(new_serial) != 0 else dados_item[2]}',
        quantity='{int(new_quantity) if len(new_quantity) != 0 else int(dados_item[3])}',
        price_unit='{float(new_price) if len(new_price) != 0 else float(dados_item[4])}'
    WHERE ID_item={id}
    """
    
    ON.query(ON.connection_ON, tab_sql)


def delete_register():
    os.system('cls')

    id = input('ID do registro a ser deletado: ')
    tb_sql = f'DELETE FROM tb_estoque WHERE ID_item={id}'

    ON.query(ON.connection_ON, tb_sql)
