# services/gestor_tarefas.py
import json
import os
from models.tarefa import Tarefa

class GestorTarefas:
    def __init__(self, caminho_json=os.path.join("data", "tarefas.json")):
        self.caminho_json = caminho_json
        self.tarefas = []
        self.proximo_id = 1
        
        os.makedirs(os.path.dirname(self.caminho_json), exist_ok=True)
        self.carregar_dados()


    def carregar_dados(self):
        if not os.path.exists(self.caminho_json):
            self.tarefas = []
            return

        try:
            with open(self.caminho_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except (json.JSONDecodeError, OSError):
            self.tarefas = []
            return

        tarefas_validas = []
        for item in dados:
            try:
                tarefas_validas.append(Tarefa.from_dict(item))
            except (KeyError, ValueError) as e:
                print(f"[Aviso] Registo ignorado por estar corrompido: {e}")

        self.tarefas = tarefas_validas
        if self.tarefas:
            self.proximo_id = max(t.id for t in self.tarefas) + 1

    def guardar_dados(self):
        try:
            with open(self.caminho_json, "w", encoding="utf-8") as f:
                json.dump([t.to_dict() for t in self.tarefas], f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"[Erro] Falha ao salvar dados: {e}")

    def adicionar_tarefa(self, titulo, disciplina, prioridade, prazo):
        nova_tarefa = Tarefa(self.proximo_id, titulo, disciplina, prioridade, prazo)
        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1
        self.guardar_dados()
        return nova_tarefa

    def atualizar_tarefa(self, id_tarefa, titulo, disciplina, prioridade, prazo, estado):
        """Atualiza todos os dados de uma tarefa existente."""
        for t in self.tarefas:
            if t.id == id_tarefa:
                t.titulo = titulo
                t.disciplina = disciplina
                t.prioridade = prioridade
                t.prazo = prazo
                t.estado = estado

                self.guardar_dados()
                
                return True
        return False

    def remover_tarefa(self, id_tarefa):
        self.tarefas = [t for t in self.tarefas if t.id != id_tarefa]
        self.guardar_dados()

    def remover_multiplas_tarefas(self, lista_ids):
        """Remove várias tarefas de uma vez só."""
        self.tarefas = [t for t in self.tarefas if t.id not in lista_ids]
        self.guardar_dados()

    def limpar_todas_tarefas(self):
        """Apaga absolutamente tudo."""
        self.tarefas = []
        self.guardar_dados()

    def pesquisar_tarefas(self, termo):
        if not termo:
            return self.tarefas
        return [t for t in self.tarefas if termo.lower() in t.titulo.lower()]