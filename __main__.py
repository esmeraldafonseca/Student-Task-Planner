from customtkinter import CTk
from services.gestor_tarefas import GestorTarefas
from ui.interface import InterfaceGrafica

def main():
    # Inicializa o motor lógico (Services) que carrega o JSON
    gestor = GestorTarefas()
    
    # Inicializa a App CustomTkinter
    root = CTk()
    
    # Inicializa a Interface Gráfica passando as dependências
    app = InterfaceGrafica(root, gestor)
    
    # Inicia o ciclo principal
    root.mainloop()

if __name__ == "__main__":
    main()