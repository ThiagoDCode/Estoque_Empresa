import connect_banco as ON
from time import sleep
import os


def new_register():
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


def consult_register(description_item=False):
    """ Faz a consulta dos dados no Banco de Dados SQL.

    Args:
        description_item (bool, optional): Se True, define a consulta por dado(item) específico. Defaults to False.
    """
    os.system('cls')

    if description_item:
        description = input('Descrição ou serial do item: ')
        
        tab_sql = f'''
        SELECT * FROM tb_estoque 
            WHERE item_identity LIKE "%{description}%" 
            OR serial_item LIKE "%{description}%"'''
        response = ON.query_select(ON.connection_ON, tab_sql)
        
        # PRINT -------------------------------------------------------------------
        tabela(response)
        # ------------------------------------------------------------------- PRINT
    else:
       tab_sql = 'SELECT * FROM tb_estoque'
       response = ON.query_select(ON.connection_ON, tab_sql)
       
       # PRINT -------------------------------------------------------------------
       tabela(response)
       # ------------------------------------------------------------------- PRINT


def update_register():
    """ Faz a consulta no Banco de Dados para atualização do item.
    """
    os.system('cls')
    
    id = input('Digite o ID do registro a ser alterado: ')
    response = ON.query_select(ON.connection_ON, 'SELECT * FROM tb_estoque WHERE ID_item='+id)
    dados_item = [response[0][1], response[0][2], response[0][3], response[0][4]]
    
    # PRINT -------------------------------------------------------------------
    tabela(response, id=True)
    # ------------------------------------------------------------------- PRINT
    
    new_item = input('Alterar descrição do item? ')
    new_serial = input('Alterar serial do item? ')
    new_quantity = input('Alterar quantidade do registro? ')
    new_price = input('Altear preço do item? ')
    
    tab_sql = f"""
    UPDATE tb_estoque SET
        item_identity='{new_item if len(new_item) != 0 else dados_item[0]}',
        serial_item='{new_serial if len(new_serial) != 0 else dados_item[1]}',
        quantity='{int(new_quantity) if len(new_quantity) != 0 else int(dados_item[2])}',
        price_unit='{float(new_price) if len(new_price) != 0 else float(dados_item[3])}'
    WHERE ID_item={id}
    """
    
    ON.query(ON.connection_ON, tab_sql)


def delete_register():
    """ Consulta o Banco de Dados e deleta o registro desejado.
    """
    os.system('cls')

    id = input('ID do registro a ser deletado: ')
    response = ON.query_select(ON.connection_ON, 'SELECT * FROM tb_estoque WHERE ID_item='+id)
    
    # PRINT -------------------------------------------------------------------
    tabela(response, id=True)
    # ------------------------------------------------------------------- PRINT
    
    delete = input('Deletar registro (S/N): ').upper()
    if delete == 'S':
        tb_sql = f'DELETE FROM tb_estoque WHERE ID_item={id}'
        ON.query(ON.connection_ON, tb_sql)
    else:
        print('\nAÇÃO CANCELADA!\n')
        sleep(1.5)


def tabela(response_sql, id=False):
    """ Função para impressão dos itens do Banco de Dados.

    Args:
        response_sql (list): Lista dos dados do retorno do SQL.
        id (bool, optional): Se True, define a impressão de dado único. Defaults to False.
    """

    if id:
        for resp in response_sql:
            print('=' * 60)
            print(f'|{resp[0]:^3}| {resp[1]:^30} |Serial N°: {resp[2]:^10}|')
            print('-' * 60)
            print(f'Quantidade: {resp[3]:<4} Preço: R${resp[4]:<4.2f} \n')
    else:
        limit = 5  # Limita a quantidade de itens exibidos por vez
        cont = 0
        for resp in response_sql:
            print('=' * 60)
            print(f'|{resp[0]:^3}| {resp[1]:^30} |Serial N°: {resp[2]:^10}|')
            print('-' * 60)
            print(f'Quantidade: {resp[3]:<4} Preço: R${resp[4]:<4.2f}\n')
            
            cont += 1
            if cont >= limit:
                cont = 0
                os.system('pause')
                os.system('cls')
        print(' SEM MAIS RESULTADOS... '.center(60, '-'))
        print()
        os.system('pause')
