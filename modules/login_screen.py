import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt
from modules.menu_screen import MenuScreen


class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Login - Oficina")
        self.master.geometry("300x150")

        tk.Label(master, text="Usuário").pack()
        self.usuario_entry = tk.Entry(master)
        self.usuario_entry.pack()

        tk.Label(master, text="Senha").pack()
        self.senha_entry = tk.Entry(master, show="*")
        self.senha_entry.pack()

        tk.Button(master, text="Entrar", command=self.verificar_login).pack()

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT senha_hash FROM usuario WHERE login = ?", (usuario,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado and bcrypt.checkpw(senha.encode(), resultado[0]):
            self.master.destroy()
            root = tk.Tk()
            MenuScreen(root)
            root.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")
