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
    """ Verifica e válida entrada de números.

    Args:
        txt (str): Texto de exibição para o usuário.
        type (_type_, optional): Determina o tipo de saída (int ou float). Defaults to int.

    Returns:
        _type_: Retorna o número validado e convertido para o tipo escolhido (int/float)
    """
    while True:
        entry = input(txt).strip()
        if entry == '':
            break
        
        if entry.replace('.', '', 1).isdigit():
            return type(entry)
        else:
            print('\nEntrada inválido, tente novamente...\n')


def validate_entry(txt: str, y, n):
    while True:
        validate = input(txt).strip().upper()
        
        if validate == y.upper():
            return True
        elif validate == n.upper():
            return False
        else:
            print(f'Entrada inválida! Por favor, responda apenas com "{y}" ou "{n}"\n')
