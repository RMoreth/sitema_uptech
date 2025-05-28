import customtkinter as ctk
from modules.menu_screen import Menu
from modules.OS_screen import OSclass
import os
import sqlite3


class App(ctk.CTk):
    """Classe principal que controla a janela do aplicativo.
    Args:
        title: STR que representa o título da janela.
        size: Tuple com 2 parametros INT que representam a largura e altura da janela.
    """

    def __init__(self, title: str, size: tuple[int, int]) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.titulo = title

        # Configurção do banco de dados
        self.db_path = "banco.db"  # Caminho do banco de dados
        self.inicializar_banco()

        self.set_base_layout()

        # Frame do menu
        self.menu_frame = Menu(
            self,
            home=self.set_home,
            os=self.set_OS,
            clientes=None,
            estoque=None,
            financeiro=None,
            relatorios=None,
        )

        # Frame divisoria

        self.divisoria = ctk.CTkFrame(self, width=2, fg_color="red")
        self.divisoria.grid(row=0, column=1, sticky="ns")

        # Frame de conteudo
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=2, columnspan=12, sticky="nsew")
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.set_home()

    def inicializar_banco(self):
        """Inicializa o banco de dados SQLite."""
        if not os.path.exists(self.db_path):
            # Cria o banco de dados e as tabelas necessárias
            conn = sqlite3.connect(self.db_path)
            with open("setup.sql", "r", encoding="utf-8") as f:
                sql_script = f.read()
                conn.executescript(sql_script)
            conn.commit()
            conn.close()
            print("Banco de dados criado e configurado com sucesso!")
        else:
            print("Banco de dados já existe")
        return sqlite3.connect(self.db_path)

    def set_base_layout(self):
        """Define o layout básico da janela."""
        self.grid_rowconfigure(0, weight=1)  # Permite que a linha 0 se expanda
        self.grid_columnconfigure(
            0, weight=1, uniform="equal")  # Coluna do menu
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(
            (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
            weight=1,
            uniform="equal",

        )

    def mudar_titulo(self, novo: str):
        """Muda o título da janela.
        Args:
            novo: STR que representa o novo título da janela.
        """
        self.title(novo)

    def clear_content_frame(self):
        """remove todos os widgets do frame de conteúdo."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def set_home(self):
        """Exibe a tela inicial no framde de conteúdo."""
        self.clear_content_frame()
        label = ctk.CTkLabel(self.content_frame,
                             text="Bem-vindo ao sistema de oficina!")
        label.grid(row=0, column=0,
                   sticky="ew", columnspan=12)

    def set_OS(self):
        """Exibe a tela de ordem de serviço no frame de conteúdo."""
        self.clear_content_frame()
        os_screen = OSclass(self.content_frame)
        os_screen.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    mainapp = App("inicio", (800, 600))
    mainapp.mainloop()
