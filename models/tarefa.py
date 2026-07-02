class Tarefa:
    """
    Representa uma tarefa académica.

    Encapsulamento: os atributos são geridos por properties com validação,
    garantindo que uma Tarefa nunca existe num estado inválido — seja
    criada pela UI, carregada do JSON, ou atualizada mais tarde.
    """

    PRIORIDADES_VALIDAS = ("Baixa", "Média", "Alta")
    ESTADOS_VALIDOS = ("Pendente", "Concluída")

    
    def __init__(self, id_tarefa, titulo, disciplina, prioridade, prazo, estado="Pendente"):
        self.id = id_tarefa
        self.titulo = titulo
        self.disciplina = disciplina
        self.prioridade = prioridade  # Baixa, Média, Alta
        self.prazo = prazo            # Formato: DD/MM/AAAA
        self.estado = estado          # Pendente ou Concluída

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        valor = (valor or "").strip()
        if len(valor) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        if not any(c.isalpha() for c in valor):
            raise ValueError("O título não pode conter apenas números ou símbolos.")
        self._titulo = valor


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