import numpy as np
import tkinter as tk
import os

class SistemaLinearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolução de Sistemas Lineares Com Números Complexos")
        
      #  root.iconbitmap("icon.ico")

        # Definir tamanho fixo e centralizar janela
        largura = 400
        altura = 400
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        root.resizable(False, False)

        # Criar frame principal centralizado
        self.frame_principal = tk.Frame(root)
        self.frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        # Label de seleção do tamanho da matriz
        tk.Label(self.frame_principal, text="Escolha o tamanho da matriz:").grid(row=0, column=0, columnspan=3, pady=10)

        # Botões para escolher o tamanho da matriz
        tk.Button(self.frame_principal, text="2x2", command=lambda: self.criar_campos(2)).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.frame_principal, text="3x3", command=lambda: self.criar_campos(3)).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.frame_principal, text="4x4", command=lambda: self.criar_campos(4)).grid(row=1, column=2, padx=5, pady=5)

        # Frame para os campos de entrada
        self.frame_matriz = tk.Frame(self.frame_principal)
        self.frame_matriz.grid(row=2, column=0, columnspan=3, pady=10)

        # Botão para resolver
        self.btn_resolver = tk.Button(self.frame_principal, text="Resolver", command=self.resolver_sistema)
        self.btn_resolver.grid(row=3, column=0, columnspan=3, pady=10)
        self.btn_resolver.config(state=tk.DISABLED)  # Desativado até escolher o tamanho da matriz

        # Label para exibir a solução
        self.label_resultado = tk.Label(self.frame_principal, text="", font=("Arial", 12, "bold"))
        self.label_resultado.grid(row=4, column=0, columnspan=3, pady=10)

        self.entradas = []  
        self.b_entradas = []  

    def criar_campos(self, tamanho):
        self.tamanho = tamanho

        # Limpa os campos antigos
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()

        # 🔴 Limpa o resultado anterior
        self.label_resultado.config(text="")

        self.entradas = []
        self.b_entradas = []

        # Criando campos de entrada para a matriz A
        tk.Label(self.frame_matriz, text=f"Matriz A ({tamanho}x{tamanho}):").grid(row=0, column=0, columnspan=tamanho)
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                entry = tk.Entry(self.frame_matriz, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                linha.append(entry)
            self.entradas.append(linha)

        # Criando campos de entrada para o vetor b (AGORA COMO COLUNA)
        tk.Label(self.frame_matriz, text="Vetor b:").grid(row=0, column=tamanho, padx=10)  # Título do vetor b ao lado da matriz

        for i in range(tamanho):
            entry = tk.Entry(self.frame_matriz, width=5)
            entry.grid(row=i+1, column=tamanho, padx=5, pady=5)  # Alinhado na coluna ao lado da matriz A
            self.b_entradas.append(entry)

        # Ativar botão de resolver
        self.btn_resolver.config(state=tk.NORMAL)

    def resolver_sistema(self):
        try:
            A = np.zeros((self.tamanho, self.tamanho), dtype=complex)
            b = np.zeros(self.tamanho, dtype=complex)

            for i in range(self.tamanho):
                for j in range(self.tamanho):
                    A[i, j] = complex(self.entradas[i][j].get())

            for i in range(self.tamanho):
                b[i] = complex(self.b_entradas[i].get())

            v = np.linalg.solve(A, b)
            self.label_resultado.config(text=f"Solução: {v}", fg="green")

        except ValueError:
            self.label_resultado.config(text="Erro: Insira apenas números válidos!", fg="red")
        except np.linalg.LinAlgError:
            self.label_resultado.config(text="Erro: A matriz não tem solução única!", fg="red")

root = tk.Tk()
icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
root.iconbitmap(icon_path)
app = SistemaLinearApp(root)
root.mainloop()
