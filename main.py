from extras import menu
import lib_functions as func
import connect_banco as ON
from time import sleep
import os

import AREA_TESTE as teste


while True:
    match menu('1:NOVO REGISTRO', '2:CONSULTAR REGISTRO', '3:ATUALIZAR REGISTRO', '4:DELETAR REGISTRO', '5:DESCONECTAR'):
        case 'DESCONECTAR':
            os.system('cls')
            print('\nPROGRAMA FINALIZADO! \n')
            sleep(1.5)
            break
        
        case 'NOVO REGISTRO':
            func.insert_register()
        
        case 'CONSULTAR REGISTRO':
            while True:
                match menu('1:TABELA GERAL', '2:DESCRIÇÃO OU SERIAL', '3:CANCELAR', menu='OPÇÕES DE CONSULTA'):
                    case 'CANCELAR':
                        break
                    
                    case 'TABELA GERAL':
                        func.consult_register()
                    
                    case 'DESCRIÇÃO OU SERIAL':
                        func.consult_register(identity=True)
    
        case 'ATUALIZAR REGISTRO':
            func.update_register()
    
        case 'DELETAR REGISTRO':
            func.delete_register()


ON.connection_ON.close()
