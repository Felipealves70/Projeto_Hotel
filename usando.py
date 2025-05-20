import tkinter as tk
from tkinter import messagebox

# Dados
hospedes = []
quartos = {101: None, 102: None, 103: None, 104: None}

# Funções
def cadastrar_hospede():
    nome = entry_nome.get()
    try:
        quarto = int(entry_quarto.get())
    except ValueError:
        messagebox.showerror("Erro", "Número de quarto inválido.")
        return

    if quarto not in quartos:
        messagebox.showerror("Erro", "Quarto inexistente.")
    elif quartos[quarto] is not None:
        messagebox.showerror("Erro", "Quarto ocupado.")
    else:
        hospedes.append({'nome': nome, 'quarto': quarto})
        quartos[quarto] = nome
        messagebox.showinfo("Sucesso", f"{nome} cadastrado no quarto {quarto}.")
        entry_nome.delete(0, tk.END)
        entry_quarto.delete(0, tk.END)

def fazer_checkout():
    try:
        quarto = int(entry_checkout.get())
    except ValueError:
        messagebox.showerror("Erro", "Número de quarto inválido.")
        return

    if quarto in quartos and quartos[quarto] is not None:
        nome = quartos[quarto]
        quartos[quarto] = None
        hospedes[:] = [h for h in hospedes if h['quarto'] != quarto]
        messagebox.showinfo("Checkout realizado", f"{nome} saiu do quarto {quarto}.")
        entry_checkout.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Quarto já está vazio ou não existe.")

def listar_reservas():
    janela_reservas = tk.Toplevel(root)
    janela_reservas.title("Reservas Atuais")
    janela_reservas.config(bg="#f0f0f0")
    tk.Label(janela_reservas, text="Hóspedes Atuais", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

    for h in hospedes:
        tk.Label(janela_reservas, text=f"{h['nome']} - Quarto {h['quarto']}", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", padx=20)

# Janela principal
root = tk.Tk()
root.title("Sistema de Hotel")
root.geometry("400x400")
root.configure(bg="#e0f7fa")

# Título
tk.Label(root, text="Sistema de Hotel", font=("Helvetica", 18, "bold"), bg="#e0f7fa", fg="#00796b").pack(pady=10)

# Frame Cadastro
frame_cadastro = tk.LabelFrame(root, text="Cadastro de Hóspedes", padx=10, pady=10, bg="#e0f7fa", fg="#004d40")
frame_cadastro.pack(padx=10, pady=10, fill="both")

tk.Label(frame_cadastro, text="Nome:", bg="#e0f7fa").grid(row=0, column=0, sticky="e")
entry_nome = tk.Entry(frame_cadastro, width=25)
entry_nome.grid(row=0, column=1, pady=5)

tk.Label(frame_cadastro, text="Quarto:", bg="#e0f7fa").grid(row=1, column=0, sticky="e")
entry_quarto = tk.Entry(frame_cadastro, width=25)
entry_quarto.grid(row=1, column=1, pady=5)

tk.Button(frame_cadastro, text="Cadastrar", bg="#00796b", fg="white", command=cadastrar_hospede).grid(row=2, columnspan=2, pady=10)

# Frame Checkout
frame_checkout = tk.LabelFrame(root, text="Checkout", padx=10, pady=10, bg="#e0f7fa", fg="#004d40")
frame_checkout.pack(padx=10, pady=10, fill="both")

tk.Label(frame_checkout, text="Quarto:", bg="#e0f7fa").grid(row=0, column=0, sticky="e")
entry_checkout = tk.Entry(frame_checkout, width=25)
entry_checkout.grid(row=0, column=1, pady=5)

tk.Button(frame_checkout, text="Fazer Checkout", bg="#d32f2f", fg="white", command=fazer_checkout).grid(row=1, columnspan=2, pady=10)

# Botão de Listar Reservas
tk.Button(root, text="Listar Reservas", bg="#388e3c", fg="white", command=listar_reservas).pack(pady=10)

root.mainloop()