def exists_word(word, instance):
    result = []
    for item in instance.queue:
        ocorrencias = []
        for j, linha in enumerate(item['linhas_do_arquivo']):
            if word.upper() in linha.upper():
                ocorrencias.append({"linha": j + 1})
        if ocorrencias != []:
            result.append({
                    "palavra": word,
                    "arquivo": item['nome_do_arquivo'],
                    "ocorrencias": ocorrencias
                })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
