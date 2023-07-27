from time import sleep
import os


def menu(*options: str, menu='OPÇÕES DE REGISTRO') -> str:
    opt_dict = {}
    for opt in options:
        opt_dict[opt.split(':')[0]] = opt.split(':')[1]
  
    while True:
        os.system('cls')
    
        tamanho = 30
        # PRINT ----------------------------------------------------------
        print(
            f'+{"=" * tamanho}+ \n'
            f'|{menu:^{tamanho}}| \n'
            f'+{"=" * tamanho}+')
        for key, value in opt_dict.items():
            print(f'|{f" [{key}] - {value.capitalize()}":{tamanho}}|')
        print(f'+{"=" * tamanho}+')
        # ---------------------------------------------------------- PRINT

        entry = input('digite a opção: ')
        if opt_dict.get(entry):
            return opt_dict[entry]
    
        print('Opção inválida, tente novamente...\n')
        sleep(1)


def number_check(txt:str, type=int):
    while True:
        entry = input(txt).strip()
        if entry == '':
            break
        
        if entry.replace('.', '', 1).isdigit():
            return type(entry)
        else:
            print('Valor inválido, tente novamente...')


if __name__ == '__main__':
    menu()
