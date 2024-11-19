class AtividadeNotFound(Exception):
    pass

atividades = []  # Lista para simular banco de dados.

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

def criar_atividade(id_disciplina, enunciado, respostas=[]):
    max_id = max([atividade['id_atividade'] for atividade in atividades], default=0)
    nova_atividade = {
        'id_atividade': max_id + 1,
        'id_disciplina': id_disciplina,
        'enunciado': enunciado,
        'respostas': respostas
    }
    atividades.append(nova_atividade)
    return nova_atividade


def atualizar_atividade(id_atividade, id_disciplina, enunciado, respostas):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividade.update({
                'id_disciplina': id_disciplina,
                'enunciado': enunciado,
                'respostas': respostas
            })
            return atividade
    raise AtividadeNotFound

def deletar_atividade(id_atividade):
    global atividades
    atividades = [atividade for atividade in atividades if atividade['id_atividade'] != id_atividade]
    if len(atividades) == len(atividades):
        raise AtividadeNotFound
