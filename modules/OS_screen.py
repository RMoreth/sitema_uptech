import customtkinter as ctk


import customtkinter as ctk


class OSclass(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")

        # Configuração do layout
        self.grid_rowconfigure(1, weight=1)  # Tabela ocupa o espaço vertical
        # Tabela ocupa o espaço horizontal
        self.grid_columnconfigure(0, weight=1)

        # Cabeçalho
        self.header_frame = ctk.CTkFrame(self, fg_color="lightgray")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.header_frame.grid_columnconfigure(1, weight=1)

        self.btn_nova_ordem = ctk.CTkButton(
            self.header_frame, text="Nova Ordem")
        self.btn_nova_ordem.grid(row=0, column=0, padx=10, pady=5)

        self.entry_busca = ctk.CTkEntry(
            self.header_frame, placeholder_text="Buscar...")
        self.entry_busca.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Tabela de ordens de serviço
        self.tabela_frame = ctk.CTkFrame(self)
        self.tabela_frame.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.tabela = ctk.CTkLabel(
            self.tabela_frame, text="Tabela de Ordens de Serviço (Exemplo)")
        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        # Detalhes da ordem de serviço
        self.detalhes_frame = ctk.CTkFrame(self, fg_color="white")
        self.detalhes_frame.grid(
            row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.detalhes_frame.grid_rowconfigure(0, weight=1)
        self.detalhes_frame.grid_columnconfigure(0, weight=1)

        self.detalhes_label = ctk.CTkLabel(
            self.detalhes_frame, text="Detalhes da Ordem de Serviço")
        self.detalhes_label.pack(fill="both", expand=True, padx=10, pady=10)
