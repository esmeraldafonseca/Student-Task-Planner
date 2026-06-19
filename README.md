# 🎓 Student Task Planner

## 📖 Sobre o Projeto

O **Student Task Planner** é uma aplicação desktop desenvolvida em Python com o objetivo de auxiliar estudantes na organização das suas atividades académicas.

Este projeto foi proposto pelo formador **Sebilson Cristóvão** como desafio prático para consolidar conhecimentos de:

- Programação Orientada a Objetos (POO)
- Desenvolvimento de interfaces gráficas
- Estruturação de projetos Python
- Persistência de dados em ficheiros JSON
- Arquitetura modular

A aplicação permite gerir tarefas académicas de forma simples e intuitiva, centralizando informações como disciplinas, prioridades, prazos e estado de conclusão.

---

## 🚀 Funcionalidades

### Gestão de Tarefas

- Criar novas tarefas académicas
- Editar tarefas existentes
- Remover tarefas individualmente
- Remover múltiplas tarefas simultaneamente
- Limpar todas as tarefas do sistema

### Organização Académica

- Definir disciplina
- Definir prioridade (Baixa, Média ou Alta)
- Definir prazo limite
- Controlar o estado da tarefa (Pendente ou Concluída)

### Pesquisa

- Pesquisa dinâmica em tempo real
- Filtragem por título da tarefa

### Persistência de Dados

- Armazenamento automático em ficheiro JSON
- Carregamento automático das tarefas ao iniciar a aplicação

---

## 🛠 Tecnologias Utilizadas

- Python 3
- CustomTkinter
- Tkinter
- JSON
- Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do Projeto

```text
StudentTaskPlanner/
│
├── data/
│   └── tarefas.json
│
├── models/
│   └── tarefa.py
│
├── services/
│   └── gestor_tarefas.py
│
├── ui/
│   └── interface.py
│
├── main.py
├── README.md
└── .gitignore
```

---

## 🏗 Arquitetura

O projeto segue uma arquitetura modular baseada na separação de responsabilidades.

### Models

Responsável pela representação das entidades do sistema.

- `Tarefa`

### Services

Responsável pela lógica de negócio e manipulação dos dados.

- `GestorTarefas`

### UI

Responsável pela interface gráfica e interação com o utilizador.

- `InterfaceGrafica`

---

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd StudentTaskPlanner
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install customtkinter pillow
```

---

## ▶️ Executar a Aplicação

```bash
python main.py
```

---

## 🎯 Objetivos de Aprendizagem

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Programação Orientada a Objetos
- Modularização de código
- Manipulação de ficheiros JSON
- Desenvolvimento de interfaces gráficas
- Validação de dados
- Gestão de estado da aplicação
- Utilização de Git e GitHub

---

## 👩‍💻 Autora

**Esmeralda Fonseca**

Projeto académico desenvolvido no âmbito da formação orientada pelo formador **Sebilson Cristóvão**.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educativos e de aprendizagem.
