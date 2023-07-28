import connect_banco as ON
import extras as EX
from sqlite3 import Error
from time import sleep
import os


def new_register():
    """ Adiciona novo item ao Banco de Dados
    """

    while True:
        os.system('cls')
        
        description = input('Descrição do item: ').strip()
        if not description:
            print('\nÉ necessário preencher a descrição do item!\n')
            os.system('pause')
            continue
        serial = input('Número serial do item: ').strip()
        quantity = EX.number_check('Quantidade para registro: ', type=int)
        if not quantity:
            quantity = 0
        price = EX.number_check('Preço do item: R$', type=float)
        if not price:
            price = 0.0
    
        insert = EX.validate_entry('\nFazer o INSERT dos dados ( S/N )? ', 'S', 'N')
        if insert:
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
        else:
            print('\nINSERT cancelado!\n')
            sleep(1.5)
        
        os.system('cls')
        new_register = EX.validate_entry('Adicionar um novo registro ( S/N )? ', 'S', 'N')
        if not new_register:
            break


def consult_register():
    """ Faz a consulta dos dados no Banco de Dados SQL.

    Args:
        description_item (bool, optional): Se True, define a consulta por dado(item) específico. Defaults to False.
    """
    while True:
        os.system('cls')
    
        description = input('Descrição ou serial do item: ')

        if description:
            try:
                tab_sql = f'''
                SELECT * FROM tb_estoque 
                    WHERE item_identity LIKE "%{description}%" 
                    OR serial_item LIKE "%{description}%"'''
                response = ON.query_select(ON.connection_ON, tab_sql)
                
                if not response:
                    print('\nRegistro não encontrado no Banco de Dados!\n')
                
                # PRINT -------------------------------------------------------------------
                tabela(response)
                # ------------------------------------------------------------------- PRINT
            except Error as erro:
                print(EX.error(erro))
        else:
            try:
                tab_sql = 'SELECT * FROM tb_estoque'
                response = ON.query_select(ON.connection_ON, tab_sql)
                
                # PRINT -------------------------------------------------------------------
                tabela(response)
                # ------------------------------------------------------------------- PRINT
            except Error as erro:
                print(EX.error(erro))

        os.system('cls')
        new_consult = EX.validate_entry('Nova consulta ( S/N )? ', 'S', 'N')
        if not new_consult:
            break


def update_register():
    """ Faz a consulta no Banco de Dados para atualização do item.
    """
    while True:
        os.system('cls')

        try:
            id = input('Digite o ID do registro a ser alterado: ')
            response = ON.query_select(ON.connection_ON, 'SELECT * FROM tb_estoque WHERE ID_item='+id)
        except (Error, TypeError, ValueError):
            print(EX.error('\nEntrada inválida!\n'))
            sleep(1.5)
        else:
            if not response:
                print('\nID de registro não encontrado no Banco de Dados!\n')
                os.system('pause')
            else:
                # PRINT -------------------------------------------------------------------
                tabela(response, id=True)
                # ------------------------------------------------------------------- PRINT

                new_item = [input('Alterar descrição do item? ').strip(), 'item_identity']
                new_serial = [input('Alterar serial do item? ').strip(), 'serial_item']
                new_quantity = [EX.number_check('Alterar quantidade do registro? '), 'quantity']
                new_price = [EX.number_check('Altear preço do item? ', type=float), 'price_unit']

                apply_update = EX.validate_entry('\nAplicar atualização (S/N): ', 'S', 'N')
                if apply_update:
                    done_up = False
                    
                    for value, coluna in [new_item, new_serial, new_quantity, new_price]:
                        if value:
                            done_up = True
                            tab_sql = f'UPDATE tb_estoque SET "{coluna}"="{value}" WHERE ID_item={id}'
                            ON.query(ON.connection_ON, tab_sql)
                
                    if not done_up:
                        print('\nNenhuma atualização feita no registro!\n')
                        sleep(1.5)
        
        os.system('cls')
        new_update = EX.validate_entry('Atualizar outro registro ( S/N )? ', 'S', 'N')
        if not new_update:
            break


def delete_register():
    """ Consulta o Banco de Dados e deleta o registro desejado.
    """
    while True:
        os.system('cls')

        try:
            id = input('ID do registro a ser deletado: ')
            response = ON.query_select(ON.connection_ON, 'SELECT * FROM tb_estoque WHERE ID_item='+id)
        except (Error):
            print('\nAÇÃO CANCELADA!'), sleep(1.5)
            break
        else:
            if not response:
                print('\nID de registro não encontrado no Banco de Dados!\n')
                os.system('pause')
            else:
                # PRINT -------------------------------------------------------------------
                tabela(response, id=True)
                # ------------------------------------------------------------------- PRINT
                
                delete = EX.validate_entry('Deletar registro (S/N): ', 'S', 'N')
                if delete:
                    tb_sql = f'DELETE FROM tb_estoque WHERE ID_item={id}'
                    ON.query(ON.connection_ON, tb_sql)
                else:
                    print('\nAÇÃO CANCELADA!\n')
                    sleep(1.5)
        
        os.system('cls')
        new_delete = EX.validate_entry('Deletar outro registro ( S/N )? ', 'S', 'N')
        if not new_delete:
            break


def tabela(response_sql, id=False):
    """ Função para impressão dos itens do Banco de Dados.

    Args:
        response_sql (list): Lista dos dados do retorno do SQL.
        id (bool, optional): Se True, define a impressão de dado único. Defaults to False.
    """
    print()
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
