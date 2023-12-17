from time import sleep
import os


def menu(*options, title="") -> int:
    """
    Menu dinâmico. Exemplo: ("Opção 1", "Opção 2", "Opção 3"...)

    Args:
        title (str, optional): Título para o Menu. Defaults to "".

    Raises:
        Exception: Retorna erro caso entrada inválida

    Returns:
        int: Retorna o número da opção
    """
    os.system("cls")
    
    print("+=============================+")
    print(f"| {title.center(27)} |")
    print("+=============================+")
    for num, opt in enumerate(options):
        print(f"| {f'[{num+1}] - {opt.upper()}':27} |")
    print("+=============================+")
    
    while True:
        try:
            resposta = int(input("> "))
            if 0 < resposta <= len(options):
                return resposta
            raise Exception()
        
        except (ValueError, Exception):
            print(error("ERRO! Opção inválida, tente novamente..."))
            sleep(1)


def number_check(txt: str, output_type=int):
    """ Verifica e válida entrada de números.

    Args:
        txt (str): Texto de exibição para o usuário.
        output_type (_type_, optional): Determina o tipo de saída (int ou float). Defaults to int.

    Returns:
        _type_: Retorna o número validado e convertido para o tipo escolhido (int/float)
    """
    
    while True:
        entry = input(txt).strip()
        if entry == '':
            break
        
        if entry.replace('.', '', 1).isdigit():
            return output_type(entry)
        else:
            print(error('\nEntrada inválido, tente novamente...\n'))


def validate_entry(txt: str, y, n):
    """
    Validação de entrada,

    Args:
        txt (str): Texto apresentado ao usuário
        y (_type_): Parâmetro para True
        n (_type_): Parâmetro para False

    Returns:
        bool: Retorna True ou False
    """
    
    while True:
        validate = input(txt).strip().upper()
        
        if validate == y.upper():
            return True
        elif validate == n.upper():
            return False
        else:
            print(error(f'Entrada inválida! Por favor, responda apenas com "{y}" ou "{n}"\n'))


def error(txt):
    return '\033[1;31m' + txt + '\033[m'
