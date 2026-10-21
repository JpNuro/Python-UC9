
import tkinter as tk
from tkinter import messagebox

def criar_formulario(titulo, incluir_operador=False):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("350x400")

    tk.Label(
        janela,
        text=titulo,
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    campos = {}

    def adicionar_campo(nome):
        tk.Label(janela, text=nome).pack()
        entrada = tk.Entry(janela)
        entrada.pack(pady=5, padx=20, fill="x")
        campos[nome] = entrada

    # Dados do equipamento
    adicionar_campo("Código do equipamento")
    adicionar_campo("Descrição")
    adicionar_campo("Quantidade")

    # Dados pessoais do operador
    if incluir_operador:
        adicionar_campo("Nome do operador")
        adicionar_campo("CPF do operador")

    def cadastrar():
        dados = {
            nome: campo.get()
            for nome, campo in campos.items()
        }

        if any(valor.strip() == "" for valor in dados.values()):
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        messagebox.showinfo(
            "Cadastro",
            "Cadastro realizado com sucesso!"
        )

    tk.Button(
        janela,
        text="Cadastrar",
        command=cadastrar
    ).pack(pady=15)


# Janela principal
app = tk.Tk()
app.title("Sistema de Equipamentos")
app.geometry("350x220")

tk.Label(
    app,
    text="Controle de Equipamentos",
    font=("Arial", 14, "bold")
).pack(pady=20)

tk.Button(
    app,
    text="Formulário 1 - Equipamentos",
    command=lambda: criar_formulario(
        "Cadastro de Equipamentos"
    )
).pack(pady=5)

tk.Button(
    app,
    text="Formulário 2 - Com Operador",
    command=lambda: criar_formulario(
        "Cadastro com Operador",
        True
    )
).pack(pady=5)

app.mainloop()
