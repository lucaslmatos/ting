import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, 'r') as file: 
            # O with garante que o arquivo será fehcado apos uso
            return file.read().split("\n")
    except FileNotFoundError:
        # O bloco try tentará encontrar o arquivo no caminho especificado,
        # caso haja algum erro irá retornar a mensagem de erro
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
