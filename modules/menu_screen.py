import tkinter as tk
from modules.cadastro_cliente import CadastroCliente


class MenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Principal")
        self.master.geometry("300x200")

        tk.Button(master, text="Clientes", width=20,
                  command=self.abrir_clientes).pack(pady=5)
        tk.Button(master, text="Sair", width=20,
                  command=master.quit).pack(pady=5)

    def abrir_clientes(self):
        self.master.destroy()
        root = tk.Tk()
        CadastroCliente(root)
        root.mainloop()
