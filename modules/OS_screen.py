import customtkinter as ctk
from tkinter import ttk
from tkcalendar import DateEntry
import json
import os


class OScadastro(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Cadastro de OS")
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.overrideredirect(False)  # Oculta a barra de titulo

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.largura = self.winfo_width()
        self.altura = self.winfo_height()

        self.tab_OS = ctk.CTkTabview(self)
        self.tab_OS.grid(row=0, column=0, sticky="nsew")

        self.tab_cliente = self.tab_OS.add("1 - Cliente")
        self.tab_dispositivo = self.tab_OS.add("2 - Dispositivo")
        self.tab_defeito = self.tab_OS.add("3 - Defeito")
        self.tab_diagnostico = self.tab_OS.add("4 - Diagnóstico")
        self.tab_admin = self.tab_OS.add("5 - Admin")

        self.criar_abas()

    def criar_abas(self):
        self.form_cliente()
        self.form_dispositivo()
        self.form_defeito()
        self.limpar_temp_json()

    def form_cliente(self):
        self.tab_cliente.grid_rowconfigure(0, weight=0)
        self.tab_cliente.grid_rowconfigure(1, weight=1)

        self.tab_cliente.grid_columnconfigure(0, weight=1)

        self.lb_dados_cliente = ctk.CTkLabel(
            self.tab_cliente,
            text="Dados do Cliente",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=30,
                weight="bold",
            ),
        )
        self.lb_dados_cliente.grid(
            row=0,
            column=0,
            padx=1,
            pady=1,
            sticky="ew",

        )
        self.frame_cliente = ctk.CTkFrame(self.tab_cliente,
                                          fg_color="#cfe2ff")
        self.frame_cliente.grid(
            row=1,
            column=0,
            padx=150,
            pady=(10, 100),
            sticky="nsew",
        )
        self.frame_cliente.grid_rowconfigure(
            0,
            weight=1,
        )

        self.frame_cliente.grid_rowconfigure(
            (1, 2, 3, 4, 5, 6, 7, 8),
            weight=0,
        )
        self.frame_cliente.grid_rowconfigure(
            9,
            weight=1,
        )

        self.frame_cliente.grid_columnconfigure(
            0,
            weight=1,

        )
        self.frame_cliente.grid_columnconfigure(
            (1, 2, 3, 4),
            weight=0,

        )

        self.frame_cliente.grid_columnconfigure(
            5,
            weight=1,
        )

        self.lb_nome_cliente = ctk.CTkLabel(
            self.frame_cliente,
            text="Nome: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"
        )
        self.lb_nome_cliente.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="e"

        )
        self.en_nome_cliente = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Nome",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=350,

        )
        self.en_nome_cliente.grid(
            row=1,
            column=2,
            padx=(2, 0),
            pady=2,
            sticky="w"

        )

        self.lb_telefone = ctk.CTkLabel(
            self.frame_cliente,
            text="Telefone: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_telefone.grid(
            row=1,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_telefone = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Telefone",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=195,


        )
        self.en_telefone.grid(
            row=1,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_email = ctk.CTkLabel(
            self.frame_cliente,
            text="Email: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_email.grid(
            row=2,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_email = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Email",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=350,


        )

        self.en_email.grid(
            row=2,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_cpf = ctk.CTkLabel(
            self.frame_cliente,
            text="CPF/CNPJ: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )

        self.lb_cpf.grid(
            row=2,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_cpf = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="CPF/CNPJ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=234,


        )
        self.en_cpf.grid(
            row=2,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_endereco = ctk.CTkLabel(
            self.frame_cliente,
            text="Endereço:",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=18,
                weight="bold",
            ),
            text_color="black"

        )

        self.lb_endereco.grid(
            row=5,
            column=1,
            padx=2,
            pady=20,
            sticky="w",
            columnspan=4
        )

        self.lb_cep = ctk.CTkLabel(
            self.frame_cliente,
            text="CEP: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )

        self.lb_cep.grid(
            row=6,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_cep = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="CEP",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=130,
        )
        self.en_cep.grid(
            row=6,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_estado = ctk.CTkLabel(
            self.frame_cliente,
            text="Estado: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )

        self.lb_estado.grid(
            row=6,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_estado = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Estado",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=50,
        )
        self.en_estado.grid(
            row=6,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_cidade = ctk.CTkLabel(
            self.frame_cliente,
            text="Cidade: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_cidade.grid(
            row=7,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_cidade = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Cidade",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=350,
        )
        self.en_cidade.grid(
            row=7,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.lb_bairro = ctk.CTkLabel(
            self.frame_cliente,
            text="Bairro: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_bairro.grid(
            row=7,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_bairro = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Bairro",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=260,
        )
        self.en_bairro.grid(
            row=7,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.lb_rua = ctk.CTkLabel(
            self.frame_cliente,
            text="Rua: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_rua.grid(
            row=8,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_rua = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Rua",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=350,
        )
        self.en_rua.grid(
            row=8,
            column=2,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.lb_numero = ctk.CTkLabel(
            self.frame_cliente,
            text="Número: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_numero.grid(
            row=8,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_numero = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Número",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=130,
        )
        self.en_numero.grid(
            row=8,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.btn_anterior = ctk.CTkButton(
            self.frame_cliente,
            text="Anterior",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            state="disabled",
        )
        self.btn_anterior.place(
            relx=0,
            rely=1.0,
            x=+23, y=-23,
            anchor="sw",
        )

        self.btn_proximo = ctk.CTkButton(
            self.frame_cliente,
            text="Próximo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            command=lambda: self.tab_OS.set("2 - Dispositivo"),

        )
        self.btn_proximo.place(
            relx=1.0,
            rely=1.0,
            x=-23, y=-23,
            anchor="se",
        )

    def form_dispositivo(self):

        self.tab_dispositivo.grid_rowconfigure(0, weight=0)
        self.tab_dispositivo.grid_rowconfigure(1, weight=1)

        self.tab_dispositivo.grid_columnconfigure(0, weight=1)

        self.lb_dados_dispositivo = ctk.CTkLabel(
            self.tab_dispositivo,
            text="Dados do Dispositivo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=30,
                weight="bold",
            ),

        )
        self.lb_dados_dispositivo.grid(
            row=0,
            column=0,
            padx=1,
            pady=1,
            sticky="ew",

        )

        self.frame_dispositivo = ctk.CTkTabview(self.tab_dispositivo,
                                                fg_color="#e2e3e5",
                                                command=self.on_tab_change)
        self.frame_dispositivo.grid(
            row=1,
            column=0,
            padx=150,
            pady=(10, 100),
            sticky="nsew",
        )

        self.tab_novo = self.frame_dispositivo.add("Novo")

        self.tab_novo.grid_rowconfigure(
            0,
            weight=1,
        )
        self.tab_novo.grid_rowconfigure(
            (1, 2, 3, 4, 5, 6),
            weight=0,
        )
        self.tab_novo.grid_rowconfigure(
            7,
            weight=1,
        )
        self.tab_novo.grid_columnconfigure(
            0,
            weight=1,

        )
        self.tab_novo.grid_columnconfigure(
            (1, 2, 3, 4),
            weight=0,

        )
        self.tab_novo.grid_columnconfigure(
            5,
            weight=1,
        )

        self.lb_tipo = ctk.CTkLabel(
            self.tab_novo,
            text="Tipo: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"
        )
        self.lb_tipo.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="e"

        )
        self.en_tipo = ctk.CTkComboBox(
            self.tab_novo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=200,
            values=[
                "escolha",
                "Desktop",
                "Notebook",
                "Impressora",
                "Celular",
                "Tablet",
                "Outro",
            ],
            dropdown_font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
        )
        self.en_tipo.grid(
            row=1,
            column=2,
            padx=(2, 0),
            pady=2,
            sticky="w"

        )
        self.en_tipo.set("escolha")

        self.lb_marca = ctk.CTkLabel(
            self.tab_novo,
            text="Marca: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_marca.grid(
            row=1,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_marca = ctk.CTkEntry(
            self.tab_novo,
            placeholder_text="Marca",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=200,
        )
        self.en_marca.grid(
            row=1,
            column=4,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_modelo = ctk.CTkLabel(
            self.tab_novo,
            text="Modelo: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_modelo.grid(
            row=2,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_modelo = ctk.CTkEntry(
            self.tab_novo,
            placeholder_text="Modelo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=200,
        )
        self.en_modelo.grid(
            row=2,
            column=2,
            padx=2,
            pady=2,
            sticky="w",
        )

        self.lb_id = ctk.CTkLabel(
            self.tab_novo,
            text="ID: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"
        )
        self.lb_id.grid(
            row=2,
            column=3,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_id = ctk.CTkEntry(
            self.tab_novo,
            placeholder_text="ID",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            width=200,
        )
        self.en_id.grid(
            row=2,
            column=4,
            padx=2,
            pady=2,
            sticky="w",
        )

        self.lb_acessorios = ctk.CTkLabel(
            self.tab_novo,
            text="Acessórios: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_acessorios.grid(
            row=3,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_acessorios = ctk.CTkTextbox(
            self.tab_novo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            height=80,
        )
        self.en_acessorios.grid(
            row=3,
            column=2,
            padx=2,
            pady=2,
            sticky="ew",
            columnspan=3,
        )

        self.lb_detalhes = ctk.CTkLabel(
            self.tab_novo,
            text="Detalhes: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_detalhes.grid(
            row=4,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_detalhes = ctk.CTkTextbox(
            self.tab_novo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            height=80,
        )
        self.en_detalhes.grid(
            row=4,
            column=2,
            padx=2,
            pady=2,
            sticky="ew",
            columnspan=3,
        )
        self.lb_condicao = ctk.CTkLabel(
            self.tab_novo,
            text="Condição: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            text_color="black"

        )
        self.lb_condicao.grid(
            row=5,
            column=1,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_condicao = ctk.CTkTextbox(
            self.tab_novo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            height=80,
        )
        self.en_condicao.grid(
            row=5,
            column=2,
            padx=2,
            pady=2,
            sticky="ew",
            columnspan=3,
        )
        self.btn_apagar = ctk.CTkButton(
            self.tab_novo,
            text="Apagar",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=16,
                weight="bold",
            ),
            command=self.apagar_campos_dispositivo,

        )
        self.btn_apagar.grid(
            row=6,
            column=2,
            pady=2,
            sticky="w",
        )
        self.btn_salvar = ctk.CTkButton(
            self.tab_novo,
            text="Salvar",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=16,
                weight="bold",
            ),
            command=self.salvar_dispositivo,
        )
        self.btn_salvar.grid(
            row=6,
            column=4,
            pady=2,
            sticky="e",
        )
        self.btn_anterior = ctk.CTkButton(
            self.tab_novo,
            text="Anterior",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            command=lambda: self.tab_OS.set("1 - Cliente"),

        )
        self.btn_anterior.place(
            relx=0,
            rely=1.0,
            x=17, y=-17,
            anchor="sw",
        )

        self.btn_proximo = ctk.CTkButton(
            self.tab_novo,
            text="Próximo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            command=lambda: self.tab_OS.set("3 - Defeito"),

        )
        self.btn_proximo.place(
            relx=1.0,
            rely=1.0,
            x=-17, y=-17,
            anchor="se",
        )

    def form_defeito(self):
        self.tab_defeito.grid_rowconfigure(0, weight=0)
        self.tab_defeito.grid_rowconfigure(1, weight=1)

        self.tab_defeito.grid_columnconfigure(0, weight=1)

        self.lb_dados_defeito = ctk.CTkLabel(
            self.tab_defeito,
            text="Descrição dos defeitos",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=30,
                weight="bold",
            ),

        )
        self.lb_dados_defeito.grid(
            row=0,
            column=0,
            padx=1,
            pady=1,
            sticky="ew",

        )
        self.frame_defeito = ctk.CTkTabview(self.tab_defeito,
                                            fg_color="#ffe5b4")
        self.frame_defeito.grid(
            row=1,
            column=0,
            padx=150,
            pady=(10, 100),
            sticky="nsew",
        )

        self.dispositivo1 = self.frame_defeito.add("Dispositivo 1")

        self.dispositivo1.grid_rowconfigure(
            0,
            weight=1,
        )
        self.dispositivo1.grid_rowconfigure(
            (1, 2, 3, 4, 5,),
            weight=0,
        )
        self.dispositivo1.grid_rowconfigure(
            6,
            weight=1,
        )
        self.dispositivo1.grid_columnconfigure(
            0,
            weight=1,
        )
        self.dispositivo1.grid_columnconfigure(
            (1, 2, 3, 4),
            weight=0,
        )
        self.dispositivo1.grid_columnconfigure(
            5,
            weight=1,
        )

        self.en_problema = ctk.CTkTextbox(
            self.dispositivo1,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=22,
                weight="bold",
            ),
            height=80,
        )
        self.dispositivo1.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="e",
        )

    def apagar_campos_dispositivo(self):
        """Apaga os campos do formulário de dispositivo."""
        self.en_tipo.set("escolha")
        self.en_marca.delete(0, "end")
        self.en_modelo.delete(0, "end")
        self.en_id.delete(0, "end")
        self.en_acessorios.delete("1.0", "end")
        self.en_detalhes.delete("1.0", "end")
        self.en_condicao.delete("1.0", "end")

    def salvar_dispositivo(self):
        # 1. Obtenha os valores de marca e modelo
        self.marca = self.en_marca.get()
        self.modelo = self.en_modelo.get()
        self.tipo = self.en_tipo.get()
        self.nome_aba = f"{self.tipo} {self.marca}/{self.modelo}"

        # 2. Crie uma nova aba
        self.nova_aba = self.frame_dispositivo.add(self.nome_aba)
        self.nova_aba.grid_rowconfigure(0, weight=1)
        self.nova_aba.grid_rowconfigure(
            (1, 2, 3, 4, 5, 6, 7, 8),
            weight=0,
        )
        self.nova_aba.grid_rowconfigure(
            9,
            weight=1,
        )
        self.nova_aba.grid_columnconfigure(
            0,
            weight=1,
        )
        self.nova_aba.grid_columnconfigure(
            (1, 2),
            weight=0,
        )
        self.nova_aba.grid_columnconfigure(
            3,
            weight=1,
        )

        # 3. Copie os dados da aba "Novo" para a nova aba, usando labels
        self.campos = [
            ("Tipo", self.tipo),
            ("Marca", self.marca),
            ("Modelo", self.modelo),
            ("ID", self.en_id.get()),
            ("Acessórios", self.en_acessorios.get("1.0", "end").strip()),
            ("Detalhes", self.en_detalhes.get("1.0", "end").strip()),
            ("Condição", self.en_condicao.get("1.0", "end").strip()),
        ]
        self.caminho_temp_dispositivo = "temp.dispostivos.json"

        if os.path.exists(self.caminho_temp_dispositivo):
            os.remove(self.caminho_temp_dispositivo)

        if os.path.exists(self.caminho_temp_dispositivo):
            with open(self.caminho_temp_dispositivo, "r", encoding="utf-8") as f:
                self.temp_json_dispositivo = json.load(f)
        else:
            self.temp_json_dispositivo = []

        self.temp_json_dispositivo.append(self.campos)
        with open(self.caminho_temp_dispositivo, 'w', encoding="utf-8") as f:
            json.dump(self.temp_json_dispositivo, f,
                      ensure_ascii=False, indent=4)

        for i, (label, valor) in enumerate(self.campos):
            ctk.CTkLabel(
                self.nova_aba,
                text=f"{label}:",
                font=ctk.CTkFont(family="Segoe UI Emoji",
                                 size=22, weight="bold"),
                text_color="black"
            ).grid(row=(i + 1), column=1, padx=2, pady=2, sticky="e")
            ctk.CTkLabel(
                self.nova_aba,
                text=valor,
                font=ctk.CTkFont(family="Segoe UI Emoji",
                                 size=18),
                text_color="darkgray"
            ).grid(row=(i + 1), column=2, padx=2, pady=2, sticky="w")

        self.frame_dispositivo.set(self.nome_aba)

        self.btn_deletar_dispositivo = ctk.CTkButton(
            self.nova_aba,
            text="Deletar",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=16,
                weight="bold",
            ),
            command=lambda: self.frame_dispositivo.delete(self.nome_aba),
        )
        self.btn_deletar_dispositivo.grid(
            row=8,
            column=1,
            pady=2,
            padx=10,
            sticky="w",
        )

        self.btn_novo_dispositivo = ctk.CTkButton(
            self.nova_aba,
            text="Novo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=16,
                weight="bold",
            ),
            command=lambda: (self.frame_dispositivo.set("Novo"),
                             self.apagar_campos_dispositivo())
        )
        self.btn_novo_dispositivo.grid(
            row=8,
            column=2,
            pady=2,
            padx=10,

            sticky="e",
        )

    def on_tab_change(self):
        self.nome_aba = self.frame_dispositivo.get()

    def carregar_dispositivos(self):
        self.lista_nomes_dispositivos = self.frame_dispositivo.tab_names()
        for dispositivo in self.lista_nomes_dispositivos:
            if dispositivo != "Novo":
                self.dados_dispositivo = {
                    "tipo": self.tipo,
                    "marca": self.marca,
                    "modelo": self.modelo,
                    "id": self.en_id.get(),
                    "acessorios": self.en_acessorios.get("1.0", ctk.END),
                    "detalhes": self.en_detalhes.get("1.0", ctk.END),
                    "condição": self.en_condicao.get("1.0", ctk.END),
                }

    def limpar_temp_json(self):
        if os.path.exists(self.caminho_temp_dispositivo):
            os.remove(self.caminho_temp_dispositivo)


class OSclass(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.set_layout()
        self.fonte_titulo = ctk.CTkFont(
            family="Segoe UI Emoji",
            size=30,
            weight="bold",
        )
        self.toplevel_window = None

    def set_layout(self):
        """Configura o layout da tela de OS."""
        # Configuração do layout interno
        self.grid_rowconfigure(0, weight=0)  # Linha do título não se expande
        # Linha dos frames se expande
        self.grid_rowconfigure((1, 2), weight=1)
        # Colunas se expandem igualmente
        self.grid_columnconfigure(0, weight=1, uniform="equal")
        self.grid_columnconfigure(1, weight=1, uniform="equal")
        self.grid_columnconfigure(2, weight=1, uniform="equal")
        self.grid_columnconfigure(3, weight=1, uniform="equal")

        self.configure(fg_color="white")

        # Label do título
        self.label_OS = ctk.CTkLabel(
            self,
            text="Ordens de Serviço",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=30,
                weight="bold",
            )
        )
        self.label_OS.grid(
            row=0,
            column=1,
            ipady=10,
            sticky="ew",
            columnspan=2
        )

        # Frame para Treeview (Ordens Abertas)
        self.frame_abertas = ctk.CTkFrame(self)
        self.frame_abertas.grid(
            row=1, column=0, ipadx=10, ipady=10, sticky="nsew", )
        self.frame_abertas.grid_rowconfigure(
            0, weight=1)  # Permite expansão vertical
        self.frame_abertas.grid_columnconfigure(
            0, weight=1)
        self.frame_abertas.grid_columnconfigure(
            1, weight=0)
        # Impede que o frame se ajuste ao tamanho do conteúdo
        self.frame_abertas.grid_propagate(False)
        # Barra de rolagem para Treeview
        self.scrollbar = ttk.Scrollbar(self.frame_abertas, orient="vertical")
        # Usando grid para a barra de rolagem
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Treeview
        self.Lista_OS_aberta = ttk.Treeview(
            self.frame_abertas,
            columns=("col0", "col1", "col2", "col3"),
            show="headings",
            height=5,
            yscrollcommand=self.scrollbar.set,  # Conecta a barra de rolagem
        )
        self.Lista_OS_aberta.heading("#0", text="")
        self.Lista_OS_aberta.heading("#1", text="ID")
        self.Lista_OS_aberta.heading("#2", text="Cliente")
        self.Lista_OS_aberta.heading("#3", text="Data Abertura")

        self.Lista_OS_aberta.column("#0", width=0, stretch=False)
        self.Lista_OS_aberta.column("#1", width=2, anchor="center")
        self.Lista_OS_aberta.column("#2", width=50, anchor="center")
        self.Lista_OS_aberta.column("#3", width=30, anchor="center")
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
            ipadx=10,
            ipady=10,
            sticky="nsew",
            columnspan=2,
        )
        self.frame_detalhes.grid_rowconfigure(
            (0, 1, 2,),
            weight=0,
        )

        self.frame_detalhes.grid_columnconfigure(
            0,
            weight=0,
        )
        self.frame_detalhes.grid_propagate(False)

        self.subframe_cliente = ctk.CTkFrame(
            self.frame_detalhes,
            fg_color="transparent",
        )
        self.subframe_cliente.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.subframe_cliente.grid_rowconfigure(
            (0, 1, 2, 3),
            weight=1,
        )

        self.subframe_cliente.grid_columnconfigure(
            0,
            weight=1,

        )
        self.subframe_cliente.grid_columnconfigure(
            1,
            weight=1,

        )
        self.subframe_cliente.grid_columnconfigure(
            2,
            weight=1,

        )
        self.subframe_cliente.grid_columnconfigure(
            3,
            weight=1,
        )

        self.lb_nome_cliente = ctk.CTkLabel(
            self.subframe_cliente,
            text="Nome: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_nome_cliente.grid(
            row=0,
            column=0,
            padx=2,
            pady=2,
            sticky="e"

        )
        self.en_nome_cliente = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Nome",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=220,
        )
        self.en_nome_cliente.grid(
            row=0,
            column=1,
            padx=(2, 0),
            pady=2,
            sticky="w"

        )

        self.lb_telefone = ctk.CTkLabel(
            self.subframe_cliente,
            text="Telefone: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_telefone.grid(
            row=0,
            column=2,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_telefone = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Telefone",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=120,

        )
        self.en_telefone.grid(
            row=0,
            column=3,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_email = ctk.CTkLabel(
            self.subframe_cliente,
            text="Email: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_email.grid(
            row=1,
            column=0,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_email = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="Email",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=220,

        )

        self.en_email.grid(
            row=1,
            column=1,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_cpf = ctk.CTkLabel(
            self.subframe_cliente,
            text="CPF/CNPJ: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )

        self.lb_cpf.grid(
            row=1,
            column=2,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_cpf = ctk.CTkEntry(
            self.subframe_cliente,
            placeholder_text="CPF/CNPJ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=120,

        )
        self.en_cpf.grid(
            row=1,
            column=3,
            padx=2,
            pady=2,
            sticky="w"
        )
        self.label_dispositivo = ctk.CTkLabel(
            self.frame_detalhes,
            text="Dados do Dispositivo",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=15,
                weight="bold",
            ),
        )
        self.label_dispositivo.grid(
            row=2,
            column=0,
            padx=1,
            pady=1,
            sticky="w",
        )

        self.subframe_dispositivo = ctk.CTkFrame(
            self.frame_detalhes,
            fg_color="transparent",
        )
        self.subframe_dispositivo.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="w",
        )

        self.subframe_dispositivo.grid_rowconfigure(
            0,
            weight=0,
        )
        self.subframe_dispositivo.grid_rowconfigure(
            (1, 2,),
            weight=0,
        )

        self.subframe_dispositivo.grid_columnconfigure(
            0,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            1,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            2,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            3,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            2,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            3,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            4,
            weight=0,
        )
        self.subframe_dispositivo.grid_columnconfigure(
            5,
            weight=0,
        )

        self.lb_tipo = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Tipo: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_tipo.grid(
            row=0,
            column=0,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_tipo = ctk.CTkComboBox(
            self.subframe_dispositivo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=100,
            values=[
                "Desktop",
                "Notebook",
                "Impressora",
                "Celular",
                "Tablet",
                "Outro"
            ],
            dropdown_font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            )
        )
        self.en_tipo.grid(
            row=0,
            column=1,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_marca = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Marca: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_marca.grid(
            row=0,
            column=2,
            padx=2,
            pady=2,
            sticky="e"
        )
        self.en_marca = ctk.CTkEntry(
            self.subframe_dispositivo,
            placeholder_text="Marca",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=80,
        )
        self.en_marca.grid(
            row=0,
            column=3,
            padx=2,
            pady=2,
            sticky="w"
        )

        self.lb_modelo = ctk.CTkLabel(
            self.subframe_dispositivo,
            text="Modelo: ",
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
        )
        self.lb_modelo.grid(
            row=0,
            column=4,
            padx=2,
            pady=2,
            sticky="e"
        )

        self.en_modelo = ctk.CTkEntry(
            self.subframe_dispositivo,
            font=ctk.CTkFont(
                family="Segoe UI Emoji",
                size=12,
                weight="bold",
            ),
            width=100,
        )
        self.en_modelo.grid(
            row=0,
            column=5,
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
            background="darkblue",
            foreground="white",
            date_pattern="dd/mm/yyyy",
        )

        # Frame de pendentes
        self.frame_pendentes = ctk.CTkFrame(self)
        self.frame_pendentes.grid(
            row=1, column=3, ipadx=10, ipady=10, sticky="nsew",)
        self.frame_pendentes.grid_rowconfigure(0, weight=1)
        self.frame_pendentes.grid_columnconfigure(0, weight=1)
        self.frame_pendentes.grid_propagate(False)

        self.scrollbar_pendentes = ttk.Scrollbar(
            self.frame_pendentes, orient="vertical")
        # Usando grid para a barra de rolagem
        self.scrollbar_pendentes.grid(row=0, column=1, sticky="ns")

        # Treeview
        self.Lista_OS_pendentes = ttk.Treeview(
            self.frame_pendentes,
            columns=("col0", "col1", "col2", "col3"),
            show="headings",
            height=5,
            yscrollcommand=self.scrollbar_pendentes.set,
        )
        self.Lista_OS_pendentes.heading("#0", text="")
        self.Lista_OS_pendentes.heading("#1", text="ID")
        self.Lista_OS_pendentes.heading("#2", text="Cliente")
        self.Lista_OS_pendentes.heading("#3", text="Data Abertura")

        self.Lista_OS_pendentes.column("#0", width=0, stretch=False)
        self.Lista_OS_pendentes.column("#1", width=2, anchor="center")
        self.Lista_OS_pendentes.column("#2", width=50, anchor="center")
        self.Lista_OS_pendentes.column("#3", width=30, anchor="center")
        # Usando grid para a Treeview
        self.Lista_OS_pendentes.grid(
            row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Configura a rolagem
        self.scrollbar_pendentes.config(command=self.Lista_OS_pendentes.yview)

        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.grid(
            row=2, column=0, ipadx=10, ipady=10, sticky="nsew", columnspan=4)
        self.frame_botoes.grid_rowconfigure(0, weight=1)
        self.frame_botoes.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.btn_nova_os = ctk.CTkButton(
            self.frame_botoes,
            text="Nova OS",
            command=self.open_os_cadastro

        )
        self.btn_nova_os.grid(
            row=0,
            column=0,
            sticky="nsew",
            ipadx=5,
            ipady=5,
        )

        self.btn_editar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Editar OS",
        )
        self.btn_editar_os.grid(
            row=0,
            column=1,
            sticky="nsew",
            ipadx=5,
            ipady=5,
        )
        self.btn_fechar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Fechar OS",
        )

        self.btn_fechar_os.grid(
            row=0,
            column=2,
            sticky="nsew",
            ipadx=5,
            ipady=5,
        )
        self.btn_excluir_os = ctk.CTkButton(
            self.frame_botoes,
            text="Excluir OS",
        )
        self.btn_excluir_os.grid(
            row=0,
            column=3,
            sticky="nsew",
            ipadx=5,
            ipady=5,
        )
        self.btn_buscar_os = ctk.CTkButton(
            self.frame_botoes,
            text="Buscar OS",
        )
        self.btn_buscar_os.grid(
            row=0,
            column=4,
            sticky="nsew",
            ipadx=5,
            ipady=5,
        )

    def open_os_cadastro(self):
        if (
            self.toplevel_window is None
            or not self.toplevel_window.winfo_exists()
        ):
            self.toplevel_window = OScadastro(self)
            self.toplevel_window.grab_set()
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()
