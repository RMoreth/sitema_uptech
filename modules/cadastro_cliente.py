import tkinter as tk
import sqlite3
from tkinter import messagebox


class CadastroCliente:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Cliente")
        self.master.geometry("300x250")

        tk.Label(master, text="Nome").pack()
        self.nome = tk.Entry(master)
        self.nome.pack()

        tk.Label(master, text="Telefone").pack()
        self.telefone = tk.Entry(master)
        self.telefone.pack()

        tk.Label(master, text="Email").pack()
        self.email = tk.Entry(master)
        self.email.pack()

        tk.Button(master, text="Salvar",
                  command=self.salvar_cliente).pack(pady=10)

    def salvar_cliente(self):
        nome = self.nome.get()
        telefone = self.telefone.get()
        email = self.email.get()

        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cliente (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        self.master.destroy()
