import customtkinter as ctk
from tkinter import ttk
from tkcalendar import DateEntry


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
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
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
            row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=6)
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
            rowspan=8
        )
        self.frame_detalhes.grid_rowconfigure(
            (0, 1, 2,),
            weight=0,
        )

        self.frame_detalhes.grid_columnconfigure(
            0,
            weight=0,
        )
        self.frame_detalhes.grid_columnconfigure(
            1,
            weight=1,
        )
        self.frame_detalhes.grid_columnconfigure(
            2,
            weight=0,
        )
        self.frame_detalhes.grid_columnconfigure(
            3,
            weight=1,
        )

        self.subframe_cliente = ctk.CTkFrame(self.frame_detalhes)
        self.subframe_cliente.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w",
            columnspan=4,
        )

        self.subframe_cliente.grid_rowconfigure(
            0,
            weight=0,
        )
        self.subframe_cliente.grid_rowconfigure(
            (1, 2),
            weight=1,
        )

        self.subframe_cliente.grid_columnconfigure(
            0,
            weight=0,
        )
        self.subframe_cliente.grid_columnconfigure(
            1,
            weight=0,
        )
        self.subframe_cliente.grid_columnconfigure(
            2,
            weight=0,
        )
        self.subframe_cliente.grid_columnconfigure(
            3,
            weight=0,
        )

        self.lb_dados_cliente = ctk.CTkLabel(
            self.subframe_cliente,
            text="Dados do Cliente",
            font=("Arial", 12, "bold"),
        )
        self.lb_dados_cliente.grid(
            row=0,
            column=0,
            padx=1,
            pady=1,
        )
        self.lb_nome_cliente = ctk.CTkLabel(
            self.subframe_cliente,
            text="Nome do Cliente",
            font=("Arial", 10, "bold"),
        )
        self.lb_nome_cliente.grid(
            row=1,
            column=0,
            padx=2,
            pady=2,
            sticky="w"

        )
        self.en_nome_cliente = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Nome do Cliente",
            font=("Arial", 10),
            width=180
        )
        self.en_nome_cliente.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="w"

        )

        self.lb_telefone = ctk.CTkLabel(
            self.subframe_cliente,
            text="Telefone",
            font=("Arial", 10, "bold"),
        )
        self.lb_telefone.grid(
            row=1,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.en_telefone = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Telefone",
            width=100,
            font=("Arial", 10),
        )
        self.en_telefone.grid(
            row=1,
            column=3,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.en_telefone.grid_propagate(False)

        self.lb_email = ctk.CTkLabel(
            self.subframe_cliente,
            text="Email",
            font=("Arial", 10, "bold"),
        )
        self.lb_email.grid(
            row=2,
            column=0,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.en_email = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Email",
            font=("Arial", 10),
            width=180
        )

        self.en_email.grid(
            row=2,
            column=1,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.subframe_dispositivo = ctk.CTkFrame(self.frame_detalhes)
        self.subframe_dispositivo.grid(
            row=1,
            column=0,
            padx=1,
            pady=11,
            sticky="ew",
            columnspan=4,
        )
        self.subframe_dispositivo.grid_rowconfigure(
            (0),
            weight=0,
        )

        self.subframe_dispositivo.grid_rowconfigure(
            (1, 2),
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            (0, 2),
            weight=0,
        )

        self.subframe_dispositivo.grid_columnconfigure(
            (1, 3),
            weight=0,
        )

        self.label_dispositivo = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Dados do Dispositivo",
            font=("Arial", 12, "bold"),
        )
        self.label_dispositivo.grid(
            row=0,
            column=0,
            padx=1,
            pady=1,
            sticky="w"
        )

        self.lb_tipo = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Tipo",
            font=("Arial", 10, "bold"),
        )
        self.lb_tipo.grid(
            row=1,
            column=0,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.en_tipo = ctk.CTkEntry(
            self.subframe_dispositivo,
            placeholder_text="Tipo",
            font=("Arial", 10),
            width=50
        )
        self.en_tipo.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_marca = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Marca",
            font=("Arial", 10, "bold"),
        )
        self.lb_marca.grid(
            row=1,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.en_marca = ctk.CTkEntry(
            self.subframe_dispositivo,
            placeholder_text="Marca",
            font=("Arial", 10),
        )
        self.en_marca.grid(
            row=1,
            column=3,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_acessorios = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Acessórios",
            font=("Arial", 10, "bold"),
        )
        self.lb_acessorios.grid(
            row=2,
            column=0,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.en_acessorios = ctk.CTkTextbox(
            self.subframe_dispositivo,
            width=100,
            height=150,
        )
        self.en_acessorios.grid(
            row=2,
            column=1,
            padx=2,
            pady=2,
            sticky="w",
        )

        self.lb_numero_os = ctk.CTkLabel(
            self.subframe_cliente,
            text="Número da OS",
            font=("Arial", 14, "bold"),
        )

        self.en_numero_os = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Número da OS",
        )

        self.lb_status = ctk.CTkLabel(
            self.frame_detalhes,
            text="Status",
            font=("Arial", 14, "bold"),
        )

        self.en_status = ctk.CTkEntry(
            self.frame_detalhes,
            placeholder_text="Status",
        )

        self.lb_descricao = ctk.CTkLabel(
            self.frame_detalhes,
            text="Descrição",
            font=("Arial", 14, "bold"),
        )

        self.en_descricao = ctk.CTkTextbox(
            self.frame_detalhes,
            width=200,
            height=100,
        )

        self.lb_equip = ctk.CTkLabel(
            self.frame_detalhes,
            text="Equipamento",
            font=("Arial", 14, "bold"),
        )

        self.en_equip = ctk.CTkEntry(
            self.frame_detalhes,
            placeholder_text="Equipamento",
        )

        self.lb_data_abertura = ctk.CTkLabel(
            self.frame_detalhes,
            text="Data Abertura",
            font=("Arial", 14, "bold"),
        )

        self.en_data_abertura = DateEntry(
            self.frame_detalhes,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="dd/mm/yyyy",
        )

        # Frame de pendentes
        self.frame_pendentes = ctk.CTkFrame(self)
        self.frame_pendentes.grid(
            row=1, column=3, padx=10, pady=10, sticky="nsew", rowspan=6)
        self.frame_pendentes.grid_rowconfigure(0, weight=1)
        self.frame_pendentes.grid_columnconfigure(0, weight=1)

        self.scrollbar_pendentes = ttk.Scrollbar(
            self.frame_pendentes, orient="vertical")
        # Usando grid para a barra de rolagem
        self.scrollbar_pendentes.grid(row=0, column=1, sticky="ns")

        # Treeview
        self.Lista_OS_pendentes = ttk.Treeview(
            self.frame_pendentes,
            columns=("col1", "col2", "col3"),
            show="headings",
            height=5,
            yscrollcommand=self.scrollbar_pendentes.set,
        )
        self.Lista_OS_pendentes.heading("#0", text="")
        self.Lista_OS_pendentes.heading("#1", text="ID")
        self.Lista_OS_pendentes.heading("#2", text="Cliente")
        self.Lista_OS_pendentes.heading("#3", text="Data Abertura")

        self.Lista_OS_pendentes.column("#0", width=0, stretch=False)
        self.Lista_OS_pendentes.column("#1", width=5, anchor="center")
        self.Lista_OS_pendentes.column("#2", width=110, anchor="center")
        self.Lista_OS_pendentes.column("#3", width=60, anchor="center")
        # Usando grid para a Treeview
        self.Lista_OS_pendentes.grid(
            row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Configura a rolagem
        self.scrollbar_pendentes.config(command=self.Lista_OS_pendentes.yview)

        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.grid(
            row=9, column=0, padx=10, pady=10, sticky="nsew", columnspan=4)
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
