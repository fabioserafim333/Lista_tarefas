import tkinter as tk
from tkinter import messagebox


class ListaDeTarefas:
    def __init__(self, root):
        self.root = root

        self.root.title("Lista de Tarefas")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1C1C1E")

        self.tarefas = []

        self.criar_interface()

    def criar_interface(self):
        # -----------------------------
        # TÍTULO
        # -----------------------------

        titulo = tk.Label(
            self.root,
            text="Minhas Tarefas",
            bg="#1C1C1E",
            fg="#FFFFFF",
            font=("Segoe UI", 28, "bold")
        )

        titulo.pack(pady=(30, 5))

        subtitulo = tk.Label(
            self.root,
            text="Organize suas tarefas de forma simples",
            bg="#1C1C1E",
            fg="#8E8E93",
            font=("Segoe UI", 11)
        )

        subtitulo.pack(pady=(0, 25))

        # -----------------------------
        # ÁREA PARA ADICIONAR TAREFA
        # -----------------------------

        frame_adicionar = tk.Frame(
            self.root,
            bg="#2C2C2E"
        )

        frame_adicionar.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        self.entrada = tk.Entry(
            frame_adicionar,
            bg="#2C2C2E",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            relief="flat",
            font=("Segoe UI", 13)
        )

        self.entrada.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 5),
            pady=15
        )

        botao_adicionar = tk.Button(
            frame_adicionar,
            text="+",
            bg="#FF9F0A",
            fg="#FFFFFF",
            activebackground="#FFB340",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 18, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.adicionar_tarefa
        )

        botao_adicionar.pack(
            side="right",
            padx=(5, 10),
            pady=10
        )

        # Permite adicionar pressionando Enter
        self.entrada.bind(
            "<Return>",
            lambda evento: self.adicionar_tarefa()
        )

        # -----------------------------
        # CONTADOR
        # -----------------------------

        self.contador = tk.Label(
            self.root,
            text="0 tarefas",
            bg="#1C1C1E",
            fg="#8E8E93",
            font=("Segoe UI", 11)
        )

        self.contador.pack(
            anchor="w",
            padx=30,
            pady=(0, 10)
        )

        # -----------------------------
        # LISTA
        # -----------------------------

        frame_lista = tk.Frame(
            self.root,
            bg="#1C1C1E"
        )

        frame_lista.pack(
            fill="both",
            expand=True,
            padx=25
        )

        self.lista = tk.Listbox(
            frame_lista,
            bg="#2C2C2E",
            fg="#FFFFFF",
            selectbackground="#48484A",
            selectforeground="#FFFFFF",
            activestyle="none",
            relief="flat",
            bd=0,
            font=("Segoe UI", 13)
        )

        self.lista.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Barra de rolagem
        scrollbar = tk.Scrollbar(
            frame_lista,
            command=self.lista.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.lista.config(
            yscrollcommand=scrollbar.set
        )

        # -----------------------------
        # BOTÕES
        # -----------------------------

        frame_botoes = tk.Frame(
            self.root,
            bg="#1C1C1E"
        )

        frame_botoes.pack(
            fill="x",
            padx=25,
            pady=20
        )

        botao_concluir = tk.Button(
            frame_botoes,
            text="Concluir",
            bg="#34C759",
            fg="#FFFFFF",
            activebackground="#4CD964",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 11),
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.concluir_tarefa
        )

        botao_concluir.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5),
            ipady=8
        )

        botao_excluir = tk.Button(
            frame_botoes,
            text="Excluir",
            bg="#FF453A",
            fg="#FFFFFF",
            activebackground="#FF6961",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 11),
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.excluir_tarefa
        )

        botao_excluir.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5,
            ipady=8
        )

        botao_limpar = tk.Button(
            frame_botoes,
            text="Limpar",
            bg="#636366",
            fg="#FFFFFF",
            activebackground="#7A7A7E",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 11),
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.limpar_tarefas
        )

        botao_limpar.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(5, 0),
            ipady=8
        )

    # -----------------------------
    # ADICIONAR TAREFA
    # -----------------------------

    def adicionar_tarefa(self):

        tarefa = self.entrada.get().strip()

        if tarefa == "":
            messagebox.showwarning(
                "Aviso",
                "Digite uma tarefa antes de adicionar."
            )
            return

        self.tarefas.append({
            "texto": tarefa,
            "concluida": False
        })

        self.entrada.delete(0, tk.END)

        self.atualizar_lista()

    # -----------------------------
    # CONCLUIR TAREFA
    # -----------------------------

    def concluir_tarefa(self):

        selecao = self.lista.curselection()

        if not selecao:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma tarefa."
            )
            return

        indice = selecao[0]

        self.tarefas[indice]["concluida"] = True

        self.atualizar_lista()

    # -----------------------------
    # EXCLUIR TAREFA
    # -----------------------------

    def excluir_tarefa(self):

        selecao = self.lista.curselection()

        if not selecao:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma tarefa."
            )
            return

        indice = selecao[0]

        del self.tarefas[indice]

        self.atualizar_lista()

    # -----------------------------
    # LIMPAR TODAS
    # -----------------------------

    def limpar_tarefas(self):

        if not self.tarefas:
            return

        resposta = messagebox.askyesno(
            "Confirmar",
            "Deseja realmente excluir todas as tarefas?"
        )

        if resposta:
            self.tarefas.clear()

            self.atualizar_lista()

    # -----------------------------
    # ATUALIZAR LISTA
    # -----------------------------

    def atualizar_lista(self):

        self.lista.delete(
            0,
            tk.END
        )

        tarefas_concluidas = 0

        for tarefa in self.tarefas:

            if tarefa["concluida"]:

                texto = "✓  " + tarefa["texto"]

                tarefas_concluidas += 1

            else:

                texto = "○  " + tarefa["texto"]

            self.lista.insert(
                tk.END,
                texto
            )

        total = len(self.tarefas)

        if total == 1:
            texto_contador = "1 tarefa"
        else:
            texto_contador = f"{total} tarefas"

        if tarefas_concluidas > 0:
            texto_contador += f" • {tarefas_concluidas} concluída(s)"

        self.contador.config(
            text=texto_contador
        )


# -----------------------------
# INICIAR PROGRAMA
# -----------------------------

janela = tk.Tk()

aplicacao = ListaDeTarefas(janela)

janela.mainloop()
