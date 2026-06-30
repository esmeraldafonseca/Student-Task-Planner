from customtkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
from services.gestor_tarefas import GestorTarefas

class InterfaceGrafica:
    def __init__(self, app, gestor: GestorTarefas):
        self.app = app
        self.gestor = gestor
        
        self.app.geometry("1024x900")
        self.app.title("Student Task Planner Desktop")
        
        # Guardar referências de checkboxes para remoção múltipla
        self.checkboxes_remocao = {}
        
        # Splash Screen inicial
        self.splash_screen = CTkFrame(self.app, fg_color="#ADD8E6")
        self.splash_screen.pack(fill="both", expand=True)
        
        logo_label = CTkLabel(self.splash_screen, text="🎓", font=("Arial", 120))
        logo_label.pack(expand=True)
        
        self.app.after(2000, self.ir_para_menu_principal)

    def limpar_ecra_conteudo(self):
        """
        Serve para destruir os frames antigos antes de desenhar o novo ecrã.
        """
        if hasattr(self, 'main_frame') and self.main_frame:
            self.main_frame.destroy()
        
        self.main_frame = CTkFrame(self.app, fg_color="#F0F4F8")
        self.main_frame.pack(fill="both", expand=True)

    def ir_para_menu_principal(self):
        self.splash_screen.pack_forget()
        self.limpar_ecra_conteudo()
        
        # Cabeçalho do Menu
        header = CTkFrame(self.main_frame, fg_color="transparent")
        header.pack(pady=40)
        CTkLabel(header, text="📚 Student Task Planner", font=("Arial", 32, "bold"), text_color="#1E293B").pack()
        CTkLabel(header, text="Gestão Académica Centralizada", font=("Arial", 14, "italic"), text_color="#64748B").pack(pady=5)
        
        # Grid de botões 2x2 centrado
        menu_grid = CTkFrame(self.main_frame, fg_color="transparent")
        menu_grid.pack(expand=True, pady=(0, 100))
        
        botoes = [
            ("Criar Tarefa", "➕", "#22C55E", "#16A34A", self.ecra_criar_tarefa, 0, 0),
            ("Visualizar Tarefas", "📋", "#3B82F6", "#2563EB", self.ecra_visualizar, 0, 1),
            ("Editar Tarefa", "✏️", "#F59E0B", "#D97706", self.ecra_editar, 1, 0),
            ("Remover Tarefa", "❌", "#EF4444", "#DC2626", self.ecra_remover, 1, 1)
        ]
        
        for texto, icone, cor, cor_hover, comando, linha, coluna in botoes:
            btn = CTkButton(menu_grid, text=f"{icone}\n\n{texto}", font=("Arial", 22, "bold"),
                            fg_color=cor, hover_color=cor_hover, width=300, height=180, corner_radius=20, command=comando)
            btn.grid(row=linha, column=coluna, padx=20, pady=20)
            
        # Botão extra para pesquisa isolada no rodapé
        btn_pesquisa = CTkButton(self.main_frame, text="🔍 Ir Para Pesquisa de Tarefas", font=("Arial", 14, "bold"), 
                                 fg_color="#64748B", hover_color="#475569", width=250, height=40, command=self.ecra_pesquisar)
        btn_pesquisa.pack(pady=20)

    def criar_botao_voltar(self, parent):
        btn = CTkButton(parent, text="⬅️ Voltar ao Menu", font=("Arial", 12, "bold"), fg_color="#64748B", hover_color="#475569", command=self.ir_para_menu_principal)
        btn.pack(anchor="w", padx=20, pady=20)

    # --- Método auxiliar reutilizável: abre o popup do calendário ---
    def calendario(self, entry):
        popup = CTkToplevel(self.app)
        popup.title("Selecionar data")
        popup_x = self.app.winfo_rootx() + 300
        popup_y = self.app.winfo_rooty() + 200
        popup.geometry(f"+{popup_x}+{popup_y}")

        current_year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day

        cal = Calendar(popup, selectmode="day", year=current_year, month=current_month, day=current_day)
        cal.pack(pady=10)

        def confirmar():
            entry.delete(0, "end")
            entry.insert(0, cal.get_date())
            popup.destroy()

        CTkButton(popup, text="Selecionar", command=confirmar).pack(pady=10)

    #1. ECRÃ: CRIAR TAREFA
    def ecra_criar_tarefa(self):
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text="Nova Tarefa Académica", font=("Arial", 26, "bold"), text_color="#1E293B").pack(pady=10)
        
        form = CTkFrame(self.main_frame, fg_color="white", corner_radius=15)
        form.pack(pady=20, padx=40, fill="both", expand=True)

        # Coluna 0 = labels (largura fixa) | Coluna 1 = inputs (expande)
        form.grid_columnconfigure(0, weight=0, minsize=220)
        form.grid_columnconfigure(1, weight=1)

        # --- Linha 0: Título ---
        CTkLabel(form, text="Título da Tarefa:", font=("Arial", 14, "bold")).grid(
            row=0, column=0, sticky="w", padx=(50, 10), pady=(30, 10))
        ent_titulo = CTkEntry(form, height=35)
        ent_titulo.grid(row=0, column=1, sticky="ew", padx=(0, 50), pady=(30, 10))

        # --- Linha 1: Disciplina ---
        CTkLabel(form, text="Disciplina:", font=("Arial", 14, "bold")).grid(
            row=1, column=0, sticky="w", padx=(50, 10), pady=10)
        ent_disc = CTkEntry(form, height=35)
        ent_disc.grid(row=1, column=1, sticky="ew", padx=(0, 50), pady=10)

        # --- Linha 2: Prioridade ---
        CTkLabel(form, text="Prioridade:", font=("Arial", 14, "bold")).grid(
            row=2, column=0, sticky="w", padx=(50, 10), pady=10)
        combo_prio = CTkComboBox(form, values=["Baixa", "Média", "Alta"], height=35, state="readonly")
        combo_prio.set("Média")
        combo_prio.grid(row=2, column=1, sticky="ew", padx=(0, 50), pady=10)

        # --- Linha 3: Prazo Limite (entry + botão calendário na mesma sub-grid) ---
        CTkLabel(form, text="Prazo Limite (DD/MM/AAAA):", font=("Arial", 14, "bold")).grid(
            row=3, column=0, sticky="w", padx=(50, 10), pady=10)

        frame_prazo = CTkFrame(form, fg_color="transparent")
        frame_prazo.grid(row=3, column=1, sticky="ew", padx=(0, 50), pady=10)
        frame_prazo.grid_columnconfigure(0, weight=1)

        ent_prazo = CTkEntry(frame_prazo, height=35, placeholder_text="Ex: 30/06/2026")
        ent_prazo.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        btn_calendar = CTkButton(frame_prazo, text="📅", width=40, height=35, command=lambda: self.calendario(ent_prazo))
        btn_calendar.grid(row=0, column=1)

        def salvar():
            titulo = ent_titulo.get().strip()
            disciplina = ent_disc.get().strip()
            prioridade = combo_prio.get()
            prazo = ent_prazo.get().strip()
            
            if not titulo or not disciplina or not prazo:
                messagebox.showerror("Erro", "Campos vazios! Preencha todo o formulário.")
                return
            try:
                datetime.strptime(prazo, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Data Inválida", "Formato correto: DD/MM/AAAA")
                return
                
            self.gestor.adicionar_tarefa(titulo, disciplina, prioridade, prazo)
            messagebox.showinfo("Sucesso", "Tarefa adicionada!")
            self.ir_para_menu_principal()

        # Botão verde adicionar no final da página
        btn_add = CTkButton(self.main_frame, text="Adicionar", fg_color="#22C55E", hover_color="#16A34A", font=("Arial", 16, "bold"), width=300, height=50, command=salvar)
        btn_add.pack(pady=30)

    # --- 2. ECRÃ: VISUALIZAR TAREFAS ---
    def ecra_visualizar(self):
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text="Lista Geral de Tarefas", font=("Arial", 26, "bold"), text_color="#1E293B").pack(pady=10)
        
        scroll = CTkScrollableFrame(self.main_frame, fg_color="white", corner_radius=10)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        if not self.gestor.tarefas:
            CTkLabel(scroll, text="Nenhuma tarefa registada.", font=("Arial", 16, "italic")).pack(pady=50)
            return
            
        for t in self.gestor.tarefas:
            row = CTkFrame(scroll, fg_color="#F8FAFC", height=50,corner_radius=5)
            row.pack(fill="x", pady=4, padx=5)
            
            txt_info = f"ID: {t.id} | {t.titulo} | Disc: {t.disciplina} | Prio: {t.prioridade} | Prazo: {t.prazo} | Estado: {t.estado}"
            cor_txt = "#0F172A" if t.estado == "Pendente" else "#94A3B8"
            
            CTkLabel(row, text=txt_info, text_color=cor_txt, height=50, font=("Arial", 18)).pack(side="left", padx=15)

    # --- 3. ECRÃ: EDITAR TAREFA ---
    def ecra_editar(self):
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text="Selecione a Tarefa para Editar", font=("Arial", 26, "bold"), text_color="#1E293B").pack(pady=10)
        
        scroll = CTkScrollableFrame(self.main_frame, fg_color="white", corner_radius=10)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        for t in self.gestor.tarefas:
            row = CTkFrame(scroll, fg_color="#F8FAFC", height=50, corner_radius=5)
            row.pack(fill="x", pady=4, padx=5)
            
            CTkLabel(row, text=f"ID: {t.id} - {t.titulo} ({t.disciplina})",height=50, font=("Arial", 18, "bold")).pack(side="left", padx=15)
            
            # Ao clicar, abre o formulário idêntico preenchido com dados antigos
            btn_edit = CTkButton(row, text="✏️ Editar", width=80, fg_color="#F59E0B", hover_color="#D97706", command=lambda obj=t: self.formulario_edicao(obj))
            btn_edit.pack(side="right", padx=15)

    def formulario_edicao(self, tarefa_alvo):
        """
        Abre o formulário idêntico ao de criar, pré-preenchido.
        """
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text=f"A Editar Tarefa ID: {tarefa_alvo.id}", font=("Arial", 26, "bold"), text_color="#1E293B").pack(pady=10)
        
        form = CTkFrame(self.main_frame, fg_color="white", corner_radius=15)
        form.pack(pady=20, padx=40, fill="both", expand=True)

        # Coluna 0 = labels (largura fixa) | Coluna 1 = inputs (expande)
        form.grid_columnconfigure(0, weight=0, minsize=220)
        form.grid_columnconfigure(1, weight=1)

        # --- Linha 0: Título ---
        CTkLabel(form, text="Título da Tarefa:", font=("Arial", 14, "bold")).grid(
            row=0, column=0, sticky="w", padx=(50, 10), pady=(30, 10))
        ent_titulo = CTkEntry(form, height=35)
        ent_titulo.insert(0, tarefa_alvo.titulo)
        ent_titulo.grid(row=0, column=1, sticky="ew", padx=(0, 50), pady=(30, 10))

        # --- Linha 1: Disciplina ---
        CTkLabel(form, text="Disciplina:", font=("Arial", 14, "bold")).grid(
            row=1, column=0, sticky="w", padx=(50, 10), pady=10)
        ent_disc = CTkEntry(form, height=35)
        ent_disc.insert(0, tarefa_alvo.disciplina)
        ent_disc.grid(row=1, column=1, sticky="ew", padx=(0, 50), pady=10)

        # --- Linha 2: Prioridade ---
        CTkLabel(form, text="Prioridade:", font=("Arial", 14, "bold")).grid(
            row=2, column=0, sticky="w", padx=(50, 10), pady=10)
        combo_prio = CTkComboBox(form, values=["Baixa", "Média", "Alta"], height=35, state="readonly")
        combo_prio.set(tarefa_alvo.prioridade)
        combo_prio.grid(row=2, column=1, sticky="ew", padx=(0, 50), pady=10)

        # --- Linha 3: Prazo Limite (entry + botão calendário na mesma sub-grid) ---
        CTkLabel(form, text="Prazo Limite:", font=("Arial", 14, "bold")).grid(
            row=3, column=0, sticky="w", padx=(50, 10), pady=10)

        frame_prazo = CTkFrame(form, fg_color="transparent")
        frame_prazo.grid(row=3, column=1, sticky="ew", padx=(0, 50), pady=10)
        frame_prazo.grid_columnconfigure(0, weight=1)

        ent_prazo = CTkEntry(frame_prazo, height=35)
        ent_prazo.insert(0, tarefa_alvo.prazo)
        ent_prazo.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        btn_calendar = CTkButton(frame_prazo, text="📅", width=40, height=35, command=lambda: self.calendario(ent_prazo))
        btn_calendar.grid(row=0, column=1)

        # --- Linha 4: Estado da Tarefa ---
        CTkLabel(form, text="Estado da Tarefa:", font=("Arial", 14, "bold")).grid(
            row=4, column=0, sticky="w", padx=(50, 10), pady=(10, 30))
        combo_estado = CTkComboBox(form, values=["Pendente", "Concluída"], height=35, state="readonly")
        combo_estado.set(tarefa_alvo.estado)
        combo_estado.grid(row=4, column=1, sticky="ew", padx=(0, 50), pady=(10, 30))
        
        def salvar_alteracoes():
            if not ent_titulo.get() or not ent_disc.get() or not ent_prazo.get():
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return
            
            self.gestor.atualizar_tarefa(tarefa_alvo.id, 
                                         ent_titulo.get(), 
                                         ent_disc.get(), 
                                         combo_prio.get(), 
                                         ent_prazo.get(), 
                                         combo_estado.get())
            messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
            self.ecra_editar()

        btn_salvar = CTkButton(self.main_frame, text="Guardar Alterações", fg_color="#22C55E", hover_color="#16A34A", font=("Arial", 16, "bold"), width=300, height=50, command=salvar_alteracoes)
        btn_salvar.pack(pady=20)

    # --- 4. ECRÃ: REMOVER TAREFA (Com Rodapé Completo de Seleções) ---
    def ecra_remover(self):
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text="Remoção Dinâmica de Tarefas", font=("Arial", 26, "bold"), text_color="#1E293B").pack(pady=10)
        
        scroll = CTkScrollableFrame(self.main_frame, fg_color="white", corner_radius=10)
        scroll.pack(fill="both", expand=True, padx=20, pady=(10, 80)) # Margem inferior para o rodapé fixa
        
        self.checkboxes_remocao = {}
        
        for t in self.gestor.tarefas:
            row = CTkFrame(scroll, fg_color="#F8FAFC", height=45, corner_radius=5)
            row.pack(fill="x", pady=3, padx=5)

            btn_remove = CTkButton(row, text="🗑️", width=80, fg_color="#DC2626", hover_color="#D90606", command=lambda id_tarefa=t.id: self._apagar_tarefa_individual(id_tarefa))
            btn_remove.pack(side="right", padx=15)
            
            # Checkbox acoplada para identificar se está selecionada
            var_check = BooleanVar()
            chk = CTkCheckBox(row, text=f"ID: {t.id} | {t.titulo} ({t.disciplina})", variable=var_check, font=("Arial", 18), height=50)
            chk.pack(side="left", padx=15, pady=10)
            
            self.checkboxes_remocao[t.id] = var_check
            
        # Rodapé de Ações Fixo em baixo
        rodape = CTkFrame(self.main_frame, fg_color="#E2E8F0", height=70)
        rodape.pack(fill="x", side="bottom")
        
        btn_sel_todos = CTkButton(rodape, text="Selecionar Todos", fg_color="#64748B", command=self.selecionar_todos_remocao)
        btn_sel_todos.pack(side="left", padx=20, pady=20)
        
        btn_del_sel = CTkButton(rodape, text="Apagar Selecionados", fg_color="#F59E0B", hover_color="#D97706", command=self.apagar_selecionados)
        btn_del_sel.pack(side="left", padx=10, pady=20)
        
        btn_del_todos = CTkButton(rodape, text="Apagar Todos", fg_color="#EF4444", hover_color="#DC2626", command=self.apagar_absolutamente_tudo)
        btn_del_todos.pack(side="right", padx=20, pady=20)

    def _apagar_tarefa_individual(self, id_tarefa):
        if messagebox.askyesno("Confirmar", "Apagar esta tarefa?"):
            self.gestor.remover_tarefa(id_tarefa)
            self.ecra_remover()

    def selecionar_todos_remocao(self):
        for var in self.checkboxes_remocao.values():
            var.set(True)

    def apagar_selecionados(self):
        
        ids_a_remover = []

        for id_t, var in self.checkboxes_remocao.items():
        # Se a variável guardada no dicionário estiver marcada (True)
            if var.get() == True:
            # Adicionamos o ID desta tarefa à nossa lista de remoção
                ids_a_remover.append(id_t)

        if not ids_a_remover:
            messagebox.showwarning("Aviso", "Nenhuma tarefa foi selecionada!")
            return
            
        if messagebox.askyesno("Confirmar", f"Pretende apagar as {len(ids_a_remover)} tarefas selecionadas?"):
            self.gestor.remover_multiplas_tarefas(ids_a_remover)
            messagebox.showinfo("Sucesso", "Tarefas removidas.")
            self.ecra_remover()

    def apagar_absolutamente_tudo(self):
        if not self.gestor.tarefas:
            return
        if messagebox.askyesno("AVISO CRÍTICO", "Tem a certeza absoluta de que quer apagar TODAS as tarefas do sistema?"):
            self.gestor.limpar_todas_tarefas()
            messagebox.showinfo("Sucesso", "Tudo foi limpo.")
            self.ecra_remover()

    # --- 5. ECRÃ COMPLEMENTAR: PESQUISAR (Página Separada) ---
    def ecra_pesquisar(self):
        self.limpar_ecra_conteudo()
        self.criar_botao_voltar(self.main_frame)
        
        CTkLabel(self.main_frame, text="Módulo de Pesquisa Isolada", font=("Arial", 
                                                                           26, "bold"), text_color="#1E293B").pack(pady=10)
        
        # Caixa superior de filtro
        search_box = CTkFrame(self.main_frame, fg_color="transparent")
        search_box.pack(fill="x", padx=40, pady=10)
        
        ent_busca = CTkEntry(search_box, placeholder_text="Digite parte do título para procurar...", 
                             width=500, height=35)
        ent_busca.pack(side="left", expand=True, padx=(0, 10))
        
        scroll_resultados = CTkScrollableFrame(self.main_frame, fg_color="white", corner_radius=10)
        scroll_resultados.pack(fill="both", expand=True, padx=40, pady=20)
        
        def realizar_busca():
            for w in scroll_resultados.winfo_children():
                w.destroy()
            
            termo = ent_busca.get().strip()
            resultados = self.gestor.pesquisar_tarefas(termo)
            
            if not resultados:
                CTkLabel(scroll_resultados, text="Nenhum resultado corresponde à busca.", font=("Arial", 22, "italic")).pack(pady=30)
                return
                
            for t in resultados:
                row = CTkFrame(scroll_resultados, fg_color="#F8FAFC", height=45)
                row.pack(fill="x", pady=3)
                CTkLabel(row, text=f"🔍 ID: {t.id} | {t.titulo} | {t.disciplina} | Prazo: {t.prazo} [{t.estado}]", height=50, font=("Arial", 18)).pack(side="left", padx=15)

        # Atualização em tempo real acoplada ao evento de soltar a tecla (KeyRelease)
        ent_busca.bind("<KeyRelease>", lambda e: realizar_busca())
        realizar_busca()