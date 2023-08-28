from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_name = path_file
    already_processed = False
    for item in instance.queue:
        if item["nome_do_arquivo"] == file_name:
            already_processed = True
            break
    if not already_processed:
        lines = txt_importer(path_file)

        file_info = {
            "nome_do_arquivo": file_name,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(file_info)
        print(file_info, file=sys.stdout)


def remove(instance):
    path_file = instance.dequeue()
    if path_file is None:
        print("Não há elementos", file=sys.stdout)
    else:
        print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout)


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
