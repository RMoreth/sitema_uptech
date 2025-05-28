import customtkinter as ctk
from PIL import Image
from modules.OS_screen import OSclass


class Menu(ctk.CTkFrame):
    """Classe que representa o menu do aplicativo.
    Args:
        master: Janela principal do aplicativo.
    """

    def __init__(
            self,
            master,
            home,
            os,
            clientes,
            estoque,
            financeiro,
            relatorios
    ):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")

        # Configura o layout do menu
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="white")
        # Camiunho das imagens
        img_path = "images/icons/"

        # Carregar as imagens

        self.ic_os = ctk.CTkImage(Image.open(
            img_path + "os.png"), size=(40, 40))
        self.ic_cadastro = ctk.CTkImage(Image.open(
            img_path + "cadastro.png"), size=(40, 40))
        self.ic_estoque = ctk.CTkImage(Image.open(
            img_path + "estoque.png"), size=(40, 40))
        self.ic_financeiro = ctk.CTkImage(Image.open(
            img_path + "financeiro.png"), size=(40, 40))
        self.ic_relatorio = ctk.CTkImage(Image.open(
            img_path + "relatorio.png"), size=(40, 40))
        self.logo = ctk.CTkImage(Image.open("images/Logo.png"), size=(70, 70))

        # Logo do menu
        self.logo_label = ctk.CTkButton(
            self, text="",
            image=self.logo,
            fg_color="transparent",
            border_spacing=0,
            width=80,
            command=home
        )
        self.logo_label.grid(row=0, column=0, pady=10, padx=0)

        # Botões do menu
        self.btn_os = ctk.CTkButton(
            self, text="OS",
            image=self.ic_os,
            compound="top",
            border_spacing=0,
            width=80,
            command=os
        )
        self.btn_os.grid(row=1, column=0, pady=10, padx=0)

        self.btn_clientes = ctk.CTkButton(
            self, text="Clientes",
            image=self.ic_cadastro,
            compound="top",
            border_spacing=0,
            width=80,
            command=clientes

        )
        self.btn_clientes.grid(row=2, column=0, pady=10, )

        self.btn_estoque = ctk.CTkButton(
            self, text="Estoque",
            image=self.ic_estoque,
            compound="top",
            border_spacing=0,
            width=80,
            command=estoque

        )
        self.btn_estoque.grid(row=3, column=0, pady=10, )

        self.btn_financeiro = ctk.CTkButton(
            self, text="Financeiro",
            image=self.ic_financeiro,
            compound="top",
            border_spacing=0,
            width=80,
            command=financeiro

        )
        self.btn_financeiro.grid(row=4, column=0, pady=10, )

        self.btn_relatorios = ctk.CTkButton(
            self, text="Relatórios",
            image=self.ic_relatorio,
            compound="top",
            border_spacing=0,
            width=80,
            command=relatorios

        )
        self.btn_relatorios.grid(
            row=4, column=0, pady=10, )
