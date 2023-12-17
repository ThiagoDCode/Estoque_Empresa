from extras import menu
import lib_functions as func
import connect_banco as ON
import os


while True:
    match menu(
        "NOVO REGISTRO", 
        "CONSULTAR REGISTRO", 
        "ATUALIZAR REGISTRO", 
        "DELETAR REGISTRO", 
        "DESCONECTAR",
        title="OPÇÕES DE REGISTRO"):

        case 5:  # DESCONECTAR
            os.system('cls')
            break
    
        case 1:  # NOVO REGISTRO
            func.new_register()

        case 2:  # CONSULTAR REGISTRO
            while True:
                match menu(
                    "CONSULTAR TABELA", 
                    "CANCELAR", 
                    title="OPÇÕES DE CONSULTA"):
                    
                    case 2:  # CANCELAR
                        break
                    
                    case 1:  # CONSULTAR TABELA
                        func.consult_register()
    
        case 3:  # ATUALIZAR REGISTRO
            func.update_register()
    
        case 4:  # DELETAR REGISTRO
            func.delete_register()


ON.connection_ON.close()
