import customtkinter as ctk
from tkinter import messagebox
import sql

class BancoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Bancário")
        self.geometry("400x400")

        self.criar_tela_cadastro()

    def criar_tela_cadastro(self):
        self.limpar_tela()

        ctk.CTkLabel(self, text="Nome: ").grid(row=0, column=0, pady=10)
        self.nome_entry = ctk.CTkEntry(self)
        self.nome_entry.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(self, text="RG: ").grid(row=1, column=0, pady=10)
        self.rg_entry = ctk.CTkEntry(self)
        self.rg_entry.grid(row=1, column=1, pady=10)

        ctk.CTkLabel(self, text="CPF: ").grid(row=2, column=0, pady=10)
        self.cpf_entry = ctk.CTkEntry(self)
        self.cpf_entry.grid(row=2, column=1, pady=10)

        ctk.CTkLabel(self, text="Data de Nascimento:").grid(row=3, column=0, pady=10)
        self.data_nascimento_entry = ctk.CTkEntry(self)
        self.data_nascimento_entry.grid(row=3, column=1, pady=10)

        ctk.CTkButton(self, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

        ctk.CTkButton(self, text="Ir para operações bancárias", command=self.criar_tela_operacao).grid(row=5, column=0, columnspan=2, pady=10)

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        rg = self.rg_entry.get()
        cpf = self.cpf_entry.get()
        data_nascimento = self.data_nascimento_entry.get()

        if nome and rg and cpf and data_nascimento:
            cliente_id = sql.obter_cliente_por_cpf(cpf)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos")

    def criar_tela_operacao(self):
        self.limpar_tela()

        ctk.CTkLabel(self, text="CPF: ").grid(row=0, column=0, pady=10)
        self.cpf_operacoes_entry = ctk.CTkEntry(self)
        self.cpf_operacoes_entry.grid(row=0, column=1, pady=10)

        ctk.CTkButton(self, text="Depositar", command=self.depositar).grid(row=1, column=0, columnspan=2, pady=10)
        ctk.CTkButton(self, text="Ver Saldo", command=self.ver_saldo).grid(row=2, column=0, columnspan=2, pady=10)

    def depositar(self):
        cpf = self.cpf_operacoes_entry.get()
        cliente_id = sql.obter_cliente_por_cpf(cpf)

        if cliente_id:
            valor = float(ctk.CTkInputDialog(title="Depósito", text="Digite o valor a depositar:").get_input())
            saldo_atual = sql.obter_saldo(cliente_id)
            novo_saldo = saldo_atual + valor
            sql.atualizar_saldo(cliente_id, novo_saldo)
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Cliente não encontrado")

    def ver_saldo(self):
        cpf = self.cpf_operacoes_entry.get()
        cliente_id = sql.obter_cliente_por_cpf(cpf)

        if cliente_id:
            saldo = sql.obter_saldo(cliente_id)
            messagebox.showinfo("Saldo", f"O saldo atual é: R$ {saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Cliente não encontrado")

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    sql.criar_banco_de_dados()
    app = BancoApp() 
    app.mainloop()
