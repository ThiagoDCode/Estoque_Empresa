from extras import menu
import lib_functions as func
import connect_banco as con
from time import sleep
import os


while True:
    match menu():
        case 5:
            os.system('cls')
            print('\nPROGRAMA FINALIZADO! \n')
            sleep(1.5)
            break

        case 1:
            func.insert_register()
        
        case 2:
            func.consult_register()
        
        case 3:
            func.update_register()
        
        case 4:
            func.delete_register()


con.conexao_on.close()
