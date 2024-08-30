import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from sql import Database
import json

class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistema Bancário Avançado")
        self.db= Database
        self.db.create_table

        #Carregar configurações e localidades
        self.load_config()
        self.load_locais()

        #Interface
        self.create_widget()

    def load_config(self):
        try:
            with open('confi.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {}

    def save_config(self):
        with open('config,json', 'w')  as file:
            json.dump(self.config, file, indent=4)

    def load_locais(self):
        try:
            with open('locais.json', 'r') as file:
                self.locais = json.load(file)
        except FileNotFoundError:
                self.locais = [] 

    def create_widget(self):
        self.label_nome = tk.Label(self.root, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1)

        self.label_rg = tk.Label(self.root, text="RG:")
        self.label_rg.grid(row=1, column=0)   
        self.entry_rg = tk.Entry(self.root)
        self.entry_rg.grid(row=1, column=1)

        self.label_cpf = tk.Label(self.root, text="CPF:")
        self.label_cpf.grid(row=2, column=0)
        self.entry_cpf = tk.Entry(self.root)
        self.entry_cpf.grid (row=2, column=1)

        self.label_data_nascimento = tk.Label(self.root, text="Data de Nascimento:")
        self.label_data_nascimento.grid(row=3, column=0)
        self.entry_data_nascimento = tk.Entry(self.root)
        self.entry_data_nascimento.grid(row=3, column=1)

        self.label_localidade_nascimento = tk.Label(self.root, text="Localidade de Nascimento")
        self.label_localidade_nascimento.grid(row=4, column=0)
        self.combobox_localidade_nascimento = ttk.Combobox(self.root, values=self.locais)
        self.combobox_localidade_nascimento.grid(row=4, column=1)

        self.button_save = tk.Button(self.root, text="Salvar Cliente", command=self.save_client)
        self.button_save.grid(row=5, column=2)

    def save_client(self):
        nome = self.entry_nome.get()
        rg = self.entry_rg.get()
        cpf = self.entry_cpf.get()
        data_nascimento = self.entry_data_nascimento.get()
        localidade_nascimento = self.combobox_localidade_nascimento.get()

        if nome and rg and cpf and data_nascimento and localidade_nascimento:
            try:
                self.db.insert_client(nome, rg, cpf, data_nascimento, localidade_nascimento)
                messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Cliente com esse RG ou CPF já existe.")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def clear_entries(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_rg.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.combobox_localidade_nascimento.set('')

    def on_closing(self):
        self.save_config()
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()