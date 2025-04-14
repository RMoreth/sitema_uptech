import customtkinter as ctk
from modules.cadastro_cliente import CadastroCliente


class Menu(ctk.CTkFrame):
    """Classe que representa o menu do aplicativo.
    Args:
        master: Janela principal do aplicativo.
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")

        # Configura o layout do menu
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Botões do menu
        self.btn_os = ctk.CTkButton(
            self, text="OS",
        )
        self.btn_os.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_clientes = ctk.CTkButton(
            self, text="Clientes",
        )
        self.btn_clientes.grid(row=1, column=0, padx=10, pady=10)

        self.btn_estoque = ctk.CTkButton(
            self, text="Estoque",
        )
        self.btn_estoque.grid(row=2, column=0, padx=10, pady=10)

        self.btn_financeiro = ctk.CTkButton(
            self, text="Financeiro",
        )
        self.btn_financeiro.grid(row=3, column=0, padx=10, pady=10)

        self.btn_relatorios = ctk.CTkButton(
            self, text="Relatórios",
        )
        self.btn_relatorios.grid(row=4, column=0, padx=10, pady=10)
