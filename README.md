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
├── screenchots/
│   └── ecra_criar_tarefa.png
│   └── ecra_editar_tarefa.png
│   └── ecra_pesquisar.png
│   └── ecra_remover.png
│   └── ecra_visualizar.png
│   └── formulario_de_edicao.png
│   └── menu_principal.png
│   └── splash_screen.png
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

### Screnshot

Responsável pela interface gráfica e interação com o utilizador.

- `ICapturas de ecra do sistema em funcionamento`

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
```bash
pip install tkcalendar
```

---

## ▶️ Executar a Aplicação

```bash
python __main__.py
```

---

## 🖼️ Imagens do projecto

<img width="1033" height="946" alt="splash_screen" src="https://github.com/user-attachments/assets/d1ce90b5-c3eb-4461-9040-6629bcfb4814" />

<img width="1033" height="946" alt="menu_inicial" src="https://github.com/user-attachments/assets/2ae08cce-f874-4b92-ba45-9a0b7b31238c" />

<img width="1034" height="948" alt="ecra_criar_tarefa" src="https://github.com/user-attachments/assets/97aa2190-8f72-49fa-a0ab-1fb31651eba4" />

<img width="1033" height="946" alt="ecra_visualizar" src="https://github.com/user-attachments/assets/ebc19cbc-4d2e-4abf-9c9f-d94f93b0da16" />

<img width="1036" height="946" alt="ecra_editar_tarefa" src="https://github.com/user-attachments/assets/cd766d46-e367-4fac-b7df-f50f966e57e5" />

<img width="1036" height="946" alt="formulario de edicao" src="https://github.com/user-attachments/assets/93d36f35-ad71-441c-9586-4500f16895cd" />

<img width="1033" height="946" alt="ecra_pesquisar" src="https://github.com/user-attachments/assets/d4709671-15c8-4a78-978f-640d23f9c8f9" />

<img width="1033" height="946" alt="ecra_remover" src="https://github.com/user-attachments/assets/514d7cf6-e4f9-4605-8272-9f0605f4854c" />


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

## 📄 Contribuições

Contribuições são bem-vindas. Por favor faça um fork do repositorio e envie um pull request com as suas melhorias
