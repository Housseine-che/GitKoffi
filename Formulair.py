import tkinter as tk
from tkinter import ttk, messagebox

def envoyer():
    nom = nom_var.get()
    email = email_var.get()
    commentaire = commentaire_text.get("1.0", tk.END).strip()

    if not nom or not email or not commentaire:
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    messagebox.showinfo("Formulaire envoyé", f"Merci {nom} ! Nous avons bien reçu votre message.")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Formulaire de contact")
fenetre.geometry("400x400")
fenetre.configure(bg="#f2f2f2")

# Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10), padding=6)

# Variables
nom_var = tk.StringVar()
email_var = tk.StringVar()

# Widgets
ttk.Label(fenetre, text="Nom complet :").pack(pady=(20, 0), anchor="w", padx=20)
ttk.Entry(fenetre, textvariable=nom_var, width=40).pack(padx=20)

ttk.Label(fenetre, text="Email :").pack(pady=(10, 0), anchor="w", padx=20)
ttk.Entry(fenetre, textvariable=email_var, width=40).pack(padx=20)

ttk.Label(fenetre, text="Commentaire :").pack(pady=(10, 0), anchor="w", padx=20)
commentaire_text = tk.Text(fenetre, height=5, width=30, wrap="word", font=("Helvetica", 10))
commentaire_text.pack(padx=20, pady=(0, 10))

ttk.Button(fenetre, text="Envoyer", command=envoyer).pack(pady=10)

# Boucle principale
fenetre.mainloop()
