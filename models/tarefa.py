class Tarefa:
    def __init__(self, id_tarefa, titulo, disciplina, prioridade, prazo, estado="Pendente"):
        self.id = id_tarefa
        self.titulo = titulo
        self.disciplina = disciplina
        self.prioridade = prioridade  # Baixa, Média, Alta
        self.prazo = prazo            # Formato: DD/MM/AAAA
        self.estado = estado          # Pendente ou Concluída

    def to_dict(self):
        """Converte o objeto Tarefa para dicionário (compatível com JSON)."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "disciplina": self.disciplina,
            "prioridade": self.prioridade,
            "prazo": self.prazo,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, dados):
        """Cria uma instância de Tarefa a partir de um dicionário."""
        return cls(
            id_tarefa=dados["id"],
            titulo=dados["titulo"],
            disciplina=dados["disciplina"],
            prioridade=dados["prioridade"],
            prazo=dados["prazo"],
            estado=dados["estado"]
        )