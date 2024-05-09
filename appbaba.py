import tkinter as tk
import customtkinter
import random
from tkinter import messagebox

# Função para adicionar um nome à lista de jogadores
def adicionar_nome():
    nome = entry_nome.get()
    if nome:
        lista_nomes.insert('end', nome + '\n')
        entry_nome.delete(0, 'end')
    else:
        customtkinter.messagebox.showwarning("Aviso", "Por favor, insira um nome válido.")

# Função para remover um nome da lista de jogadores
def remover_nome():
    try:
        selected_indices = lista_nomes.tag_ranges("sel")
        if selected_indices:
            for i in range(0, len(selected_indices), 2):
                start = selected_indices[i]
                end = selected_indices[i + 1]
                lista_nomes.delete(start, end)
    except:
        customtkinter.messagebox.showwarning("Aviso", "Por favor, selecione um jogador para remover.")

# Função para sortear times e exibir os resultados em uma nova janela
def sortear_times():
    nomes = lista_nomes.get("1.0", "end-1c").split('\n')  # Obtém os nomes da lista
    nomes = [nome.strip() for nome in nomes if nome.strip()]  # Remove nomes vazios e espaços em branco

    if len(nomes) < 10:
        customtkinter.messagebox.showwarning("Aviso", "É preciso ter pelo menos 10 jogadores para sortear times.")
    else:
        random.shuffle(nomes)  # Embaralha a lista de nomes
        time1 = ', '.join(nomes[:5])
        time2 = ', '.join(nomes[5:10])

        # Criar uma nova janela para exibir os times sorteados
        nova_janela = customtkinter.CTkToplevel(janela)
        nova_janela.title("Times Sorteados")
        nova_janela.geometry('400x200')

        # Labels para exibir os times na nova janela
        label_time1 = customtkinter.CTkLabel(nova_janela, text=f"Time 1: {time1}")
        label_time1.pack()

        label_time2 = customtkinter.CTkLabel(nova_janela, text=f"Time 2: {time2}")
        label_time2.pack()

def novo_sorteio():
    global time1, time2
    lista_nomes.delete("1.0", "end")  # Limpar a lista de nomes
    time1 = ""
    time2 = ""


# Configuração da janela principal
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.title("Aposentados FC")
janela.geometry('600x450')

# Rótulo e campo de entrada para adicionar jogadores
label_nome = customtkinter.CTkLabel(janela, text="Nome dos Jogadores:")
label_nome.pack()
entry_nome = customtkinter.CTkEntry(janela)
entry_nome.pack()

# Botão para adicionar jogadores
botao_adicionar = customtkinter.CTkButton(janela, text="Adicionar Jogador", command=adicionar_nome)
botao_adicionar.pack()

# Lista de jogadores na biblioteca
lista_nomes = customtkinter.CTkTextbox(janela)
lista_nomes.pack()

# Botão para remover jogadores
botao_remover = customtkinter.CTkButton(janela, text="Remover Jogador", command=remover_nome)
botao_remover.pack(padx=7, pady=7)

# Botão para sortear times
botao_sortear = customtkinter.CTkButton(janela, text="Sortear Times", command=sortear_times)
botao_sortear.pack(padx=7, pady=7)

botao_novosorteio = customtkinter.CTkButton(janela, text="Novo Sorteio", command=novo_sorteio)
botao_novosorteio.pack(padx=7, pady=7)

janela.mainloop()
