from time import sleep
import os


def menu():
    while True:
        os.system('cls')
    
        tamanho = 50
        # PRINT ----------------------------------------------------------
        print(
            f'+{"=" * tamanho}+ \n'
            f'|{"OPÇÕES DE REGISTRO":^{tamanho}}| \n'
            f'+{"=" * tamanho}+')
        print(
            f'| [1] Novo Registro         [2] Consultar Registro | \n'
            f'| [3] Atualizar Registro    [4] Deletar Registro   | \n'
            f'| [5] Desconectar                                  |')
        print(f'+{"=" * tamanho}+')
        # ---------------------------------------------------------- PRINT
    
        try:
            entry = int(input('digite a opção: '))
            if entry < 0 or entry > 6:
                raise Exception()
        except (ValueError, Exception):
            print('Opção inválida, tente novamente...\n')
            sleep(1)
        else:
            return entry


if __name__ == '__main__':
    menu()
