import customtkinter as tk
from tkinter import messagebox
import tkinter as ttk

tk.set_appearance_mode('dark')

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("500x750")
        self.canvas = None
        self.errors = 0
        self.dict = {
            'Iniciante': {'gato': 'É um animal de estimação'},
            'Amador': {'mesa': 'É um móvel com 4 pernas'},
            'Semi-Pro': {'aviao': 'Meio de transporte no ar'},
            'Profissional': {'algoritmo': 'Programação e algoritmos'},
            'Internacional': {'diplomacia': 'Relações globais'},
            'Lendário': {'neurociencia': 'Ciência do estudo do cérebro'},
            'Pesadelo': {'hipopotomonstrosesquipedaliofobia': 'Extremamente longa'}
        }
        self.placaLabel = tk.CTkLabel(self.root, text="Jogo da Forca", font=('Times New Roman', 35, 'italic'))
        self.placaLabel.pack(pady=15)
        self.nomeJogador = tk.CTkEntry(self.root,state='normal', width=200, height=30, placeholder_text="Insira seu nome")
        self.nomeJogador.pack(pady=15)
        self.dificuldadeLabel = tk.CTkLabel(self.root, text="Dificuldade", font=('Times New Roman',20, 'italic'))
        self.dificuldadeLabel.pack(pady=5)
        self.dificuldadeEscolhida = tk.StringVar()
        self.dificuldadeCombobox = tk.CTkComboBox(self.root, width=200, height=30, state='readonly', variable=self.dificuldadeEscolhida, values=['Iniciante','Amador','Semi-Pro','Profissional','Internacional','Lendário','Pesadelo'])
        self.dificuldadeCombobox.pack()
        self.iniciarButton = tk.CTkButton(self.root,width=175, height=30, text="Iniciar Jogo", font=('Times New Roman', 15, 'bold'), command=self.iniciarJogo)
        self.iniciarButton.pack(pady=25)
        self.dicaLabel = tk.CTkLabel(self.root, text="", font=('Times New Roman', 15, 'italic'))
        self.dicaLabel.pack()

        self.letras_adivinhadas = set()
        self.palavra_atual = ''
        self.dica_atual = ''

    def iniciarJogo(self):
        self.nome = self.nomeJogador.get().title()
        dificuldade = self.dificuldadeEscolhida.get()
        if not self.nome or not dificuldade:
            messagebox.showwarning("Erro", "Por favor, preencha seu nome e escolha uma dificuldade.")
            return
        
        self.palavra_atual, self.dica_atual = self.obterPalavraEDica(dificuldade)

        self.dicaLabel.configure(text=f'Olá {self.nome}, a dica é: {self.dica_atual}', font=('Times New Roman', 15, 'italic'))
        self.nomeJogador.configure(state='disabled')
        self.dificuldadeCombobox.configure(state='disabled')
        self.iniciarButton.configure(state='disabled')

        self.adicionarInterface()

    def obterPalavraEDica(self, dificuldade):
        palavra_dict = self.dict.get(dificuldade)
        if palavra_dict:
            palavra, dica = palavra_dict.popitem()
            return palavra, dica
        return "", ""
    
    def adicionarInterface(self):
        self.letraEntry = tk.CTkEntry(self.root, placeholder_text='Digite uma letra...')
        self.letraEntry.pack(pady=5)

        self.verificarButton = tk.CTkButton(self.root, text='Inserir letra', command=self.verificarLetra, font=('Times New Roman', 15, 'bold'))
        self.verificarButton.pack(pady=10)

        self.canvas = ttk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        # Desenhe o poste vertical e a barra horizontal
        self.canvas.create_line(100, 50, 100, 250)
        self.canvas.create_line(100, 50, 250, 50)

    def reiniciarJogo(self):
        self.dificuldadeCombobox.configure(state='readonly')
        self.dificuldadeCombobox.set('')
        self.nomeJogador.configure(state='normal')
        self.nomeJogador.delete(0, tk.END)
        self.iniciarButton.configure(state='normal')
        self.dicaLabel.configure(text='')
        self.letraEntry.destroy()
        self.verificarButton.destroy()
        self.canvas.destroy()
        self.errors = 0
        self.letras_adivinhadas = set()

    def verificarLetra(self):
        letraInserida = self.letraEntry.get().lower()
        if letraInserida.isalpha() and len(letraInserida) == 1:
            if letraInserida in self.letras_adivinhadas:
                messagebox.showinfo('Aviso', 'Você já tentou essa letra.')
                self.letraEntry.delete(0, tk.END)
            else:
                self.letras_adivinhadas.add(letraInserida)
                if letraInserida in self.palavra_atual:
                    self.atualizarPalavraMascarada()
                    self.letraEntry.delete(0, tk.END)
                    if '_' not in self.dicaLabel.cget('text'):
                        messagebox.showinfo('Fim de jogo', f'Parabéns, você venceu! A palavra era: {self.palavra_atual}')
                        self.reiniciarJogo()
                else:
                    self.errors += 1
                    self.desenharBoneco()
                    self.letraEntry.delete(0, tk.END)
        else:
            messagebox.showerror('Erro!', 'Digite uma letra válida.')
            self.letraEntry.delete(0, tk.END)

    def atualizarPalavraMascarada(self):
        palavra_mascarada = ''
        for letra in self.palavra_atual:
            if letra in self.letras_adivinhadas:
                palavra_mascarada += letra
            else:
                palavra_mascarada += '_ '
        self.dicaLabel.configure(text=f'Palavra: {palavra_mascarada}')

    def desenharBoneco(self):
        if self.errors == 1:
            # Desenhe a cabeça
            self.canvas.create_oval(230, 100, 270, 140)
        elif self.errors == 2:
            # Desenhe o corpo
            self.canvas.create_line(250, 140, 250, 250)
        elif self.errors == 3:
            # Desenhe o braço esquerdo
            self.canvas.create_line(250, 160, 280, 190)
        elif self.errors == 4:
            # Desenhe o braço direito
            self.canvas.create_line(250, 160, 220, 190)
        elif self.errors ==5:
            # Desenhe a perna esquerda
            self.canvas.create_line(250, 250, 280, 280)
        elif self.errors == 6:
            # Desenhe a perna direita
            self.canvas.create_line(250, 250, 220, 280)

        if self.errors == 6:
            messagebox.showinfo('Fim de Jogo', f'Você perdeu! A palavra era: {self.palavra_atual}')
            self.reiniciarJogo()

    def iniciarInterface(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.CTk()
    jogo = JogoDaForca(root)
    jogo.iniciarInterface()