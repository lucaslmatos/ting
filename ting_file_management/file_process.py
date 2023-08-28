from ting_file_management.file_management import txt_importer


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
        print(file_info)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
