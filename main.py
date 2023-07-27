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
            break
    
        case 'NOVO REGISTRO':
            func.new_register()

        case 'CONSULTAR REGISTRO':
            while True:
                match menu('1:CONSULTAR TABELA', '2:CANCELAR', menu='OPÇÕES DE CONSULTA'):
                    case 'CANCELAR':
                        break
                    
                    case 'CONSULTAR TABELA':
                        func.consult_register()
    
        case 'ATUALIZAR REGISTRO':
            func.update_register()
    
        case 'DELETAR REGISTRO':
            func.delete_register()


ON.connection_ON.close()
