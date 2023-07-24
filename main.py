from extras import menu
import lib_functions as func
import connect_banco as ON
import AREA_TESTE as teste
from time import sleep
import os


while True:
    match menu('1:Novo Registro', '2:Consultar Registro', '3:Atualizar Registro', '4:Deletar Registro', '5:Desconectar'):
        case 'Desconectar':
            os.system('cls')
            print('\nPROGRAMA FINALIZADO! \n')
            sleep(1.5)
            break

        case 'Novo Registro':
            func.insert_register()
        
        case 'Consultar Registro':
            while True:
                match menu('1:Tabela Geral', '2:Descrição ou Serial', '3:Cancelar', menu='OPÇÕES DE CONSULTA'):
                    case 'Cancelar':
                        break
                    
                    case 'Tabela Geral':
                        func.consult_for()
                    
                    case 'Descrição ou Serial':
                        func.consult_for(identity=True)
                    
        case 'Atualizar Registro':
            func.update_register()
        
        case 'Deletar Registro':
            func.delete_register()


ON.conexao_on.close()
