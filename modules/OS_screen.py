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
        self.grid_rowconfigure(
            (0, 1), weight=0)  # Linha da Treeview não se expande
        # Colunas se expandem igualmente
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.configure(fg_color="white")

        # Label
        self.label_OS = ctk.CTkLabel(
            self,
            text="Ordens de Serviço",
            font=("Arial", 30, "bold"),
        )
        self.label_OS.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

        # Frame para Treeview
        self.frame_abertas = ctk.CTkFrame(
            self, width=300, height=200)  # Tamanho fixo
        self.frame_abertas.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew")
        # Impede que o frame se expanda
        self.frame_abertas.grid_propagate(False)

        # Barra de rolagem para Treeview
        self.scrollbar = ttk.Scrollbar(self.frame_abertas, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.Lista_OS_aberta = ttk.Treeview(
            self.frame_abertas,
            columns=("ID", "Cliente", "Data Abertura", "Status"),
            show="headings",
            yscrollcommand=self.scrollbar.set,  # Conecta a barra de rolagem
        )
        self.Lista_OS_aberta.heading("ID", text="ID")
        self.Lista_OS_aberta.heading("Cliente", text="Cliente")
        self.Lista_OS_aberta.heading("Data Abertura", text="Data Abertura")
        self.Lista_OS_aberta.heading("Status", text="Status")
        self.Lista_OS_aberta.pack(fill="both", expand=True, padx=5, pady=5)

        # Configura a rolagem
        self.scrollbar.config(command=self.Lista_OS_aberta.yview)

        # Frame de detalhes
        self.frame_detalhes = ctk.CTkFrame(self, width=300, height=200)
        self.frame_detalhes.grid(
            row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Frame de pendentes
        self.frame_pendentes = ctk.CTkFrame(self, width=300, height=200)
        self.frame_pendentes.grid(
            row=1, column=2, padx=10, pady=10, sticky="nsew")
