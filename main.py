from extras import menu
import lib_functions as func
import connect_banco as con
from time import sleep
import os


while True:
    menu()
    options = int(input('Opção: '))

    if options == 6:
        os.system('cls')
        print('PROGRAMA FINALIZADO! \n')
        sleep(1.5)
        break

    elif options == 1:
        func.insert_register()

    elif options == 2:
        func.consult_register()

    elif options == 3:
        func.consult_for_ident()

    elif options == 4:
        func.update_register()

    elif options == 5:
        func.delete_register()


con.conexao_on.close()
