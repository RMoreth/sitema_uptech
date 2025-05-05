import customtkinter as ctk
from tkinter import ttk


class OSclass(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        self.set_layout()

    def set_layout(self):
        """Configura o layout da tela de OS."""
        # Configuração do layout interno
        self.grid_rowconfigure(0, weight=0)  # Linha do título não se expande
        # Linha dos frames se expande
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6), weight=1)
        # Colunas se expandem igualmente
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.configure(fg_color="white")

        # Label do título
        self.label_OS = ctk.CTkLabel(
            self,
            text="Ordens de Serviço",
            font=("Arial", 30, "bold"),
        )
        self.label_OS.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")

        # Frame para Treeview (Ordens Abertas)
        self.frame_abertas = ctk.CTkFrame(self)
        self.frame_abertas.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)
        self.frame_abertas.grid_rowconfigure(
            0, weight=1)  # Permite expansão vertical
        self.frame_abertas.grid_columnconfigure(
            0, weight=1)  # Permite expansão horizontal

        # Barra de rolagem para Treeview
        self.scrollbar = ttk.Scrollbar(self.frame_abertas, orient="vertical")
        # Usando grid para a barra de rolagem
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Treeview
        self.Lista_OS_aberta = ttk.Treeview(
            self.frame_abertas,
            columns=("col1", "col2", "col3"),
            show="headings",
            height=5,
            yscrollcommand=self.scrollbar.set,  # Conecta a barra de rolagem
        )
        self.Lista_OS_aberta.heading("#0", text="")
        self.Lista_OS_aberta.heading("#1", text="ID")
        self.Lista_OS_aberta.heading("#2", text="Cliente")
        self.Lista_OS_aberta.heading("#3", text="Data Abertura")

        self.Lista_OS_aberta.column("#0", width=0, stretch=False)
        self.Lista_OS_aberta.column("#1", width=5, anchor="center")
        self.Lista_OS_aberta.column("#2", width=110, anchor="center")
        self.Lista_OS_aberta.column("#3", width=60, anchor="center")
        # Usando grid para a Treeview
        self.Lista_OS_aberta.grid(
            row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Configura a rolagem
        self.scrollbar.config(command=self.Lista_OS_aberta.yview)

        # Frame de detalhes
        self.frame_detalhes = ctk.CTkFrame(self)
        self.frame_detalhes.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew",
            columnspan=2,
            rowspan=5
        )
        self.frame_detalhes.grid_rowconfigure(0, weight=1)
        self.frame_detalhes.grid_columnconfigure(0, weight=1)

        # Frame de pendentes
        self.frame_pendentes = ctk.CTkFrame(self)
        self.frame_pendentes.grid(
            row=1, column=3, padx=10, pady=10, sticky="nsew", rowspan=3)
        self.frame_pendentes.grid_rowconfigure(0, weight=1)
        self.frame_pendentes.grid_columnconfigure(0, weight=1)

        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.grid(
            row=6, column=0, padx=10, pady=10, sticky="nsew", columnspan=4)
        self.frame_botoes.grid_rowconfigure(0, weight=1)
        self.frame_botoes.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.btn_nova_os = ctk.CTkButton(
            self.frame_botoes,
            text="Nova OS",
        )
        self.btn_nova_os.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5,
        )

        self.btn_editar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Editar OS",
        )
        self.btn_editar_os.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5,
        )
        self.btn_fechar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Fechar OS",
        )

        self.btn_fechar_os.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=5,
            pady=5,
        )
        self.btn_excluir_os = ctk.CTkButton(
            self.frame_botoes,
            text="Excluir OS",
        )
        self.btn_excluir_os.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=5,
            pady=5,
        )
        self.btn_buscar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Buscar OS",
        )
        self.btn_buscar_os.grid(
            row=0,
            column=4,
            sticky="nsew",
            padx=5,
            pady=5,
        )
