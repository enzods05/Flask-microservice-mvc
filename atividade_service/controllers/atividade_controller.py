from flask import Blueprint, jsonify, request
from models import atividade_model
from clients.pessoa_service_client import PessoaServiceClient

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    print("Rota POST /atividades/ acessada.")
    print(f"Método: {request.method}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.data}")
    dados = request.get_json()
    try:
        nova_atividade = atividade_model.criar_atividade(
            id_disciplina=dados['id_disciplina'],
            enunciado=dados['enunciado'],
            respostas=dados.get('respostas', [])
        )
        return jsonify(nova_atividade), 201
    except KeyError as e:
        return jsonify({'erro': f'Campo obrigatório ausente: {e}'}), 400


@atividade_bp.route('/<int:id_atividade>/', methods=['PUT'])
def atualizar_atividade(id_atividade):
    dados = request.get_json()
    try:
        atividade_atualizada = atividade_model.atualizar_atividade(
            id_atividade=id_atividade,
            id_disciplina=dados['id_disciplina'],
            enunciado=dados['enunciado'],
            respostas=dados.get('respostas', [])
        )
        return jsonify(atividade_atualizada), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    except KeyError as e:
        return jsonify({'erro': f'Campo obrigatório ausente: {e}'}), 400


@atividade_bp.route('/<int:id_atividade>/', methods=['DELETE'])
def deletar_atividade(id_atividade):
    try:
        atividade_model.deletar_atividade(id_atividade)
        return jsonify({'mensagem': 'Atividade excluída com sucesso'}), 200
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
