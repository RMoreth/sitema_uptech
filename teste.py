import tkinter as tk

root = tk.Tk()
erros = ["Erro A", "Erro B", "Erro C"]
checkbox_vars = []


def atualizar_erros():
    selecionados = [erros[i]
                    for i, var in enumerate(checkbox_vars) if var.get() == 1]
    print("Selecionados:", selecionados)


for i, erro in enumerate(erros):
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=erro, variable=var,
                         command=atualizar_erros)
    chk.grid(row=i, column=0, sticky="w")
    checkbox_vars.append(var)

root.mainloop()
