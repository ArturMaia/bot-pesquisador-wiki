import tkinter as tk
from tkinter import messagebox
import wikipedia

wikipedia.set_lang("pt")

def buscar():
    termo = entrada.get()
    if not termo.strip():
        messagebox.showwarning("Aviso", "Digite algo para pesquisar.")
        return
    try:
        resultado = wikipedia.summary(termo, sentences=3)
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, resultado)
    except wikipedia.exceptions.DisambiguationError as e:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, f"Termo ambíguo. Exemplos: {', '.join(e.options[:3])}")
    except wikipedia.exceptions.PageError:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, "Nenhuma página encontrada.")
    except Exception as e:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, f"Erro: {str(e)}")

janela = tk.Tk()
janela.title("Bot Wikipédia")
janela.geometry("400x500")

entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10, padx=10, fill=tk.X)

botao = tk.Button(janela, text="Pesquisar", command=buscar, font=("Arial", 12))
botao.pack(pady=5)

texto_frame = tk.Frame(janela)
texto_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(texto_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

texto = tk.Text(texto_frame, wrap=tk.WORD, yscrollcommand=scroll.set, font=("Arial", 12))
texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll.config(command=texto.yview)

janela.mainloop()
