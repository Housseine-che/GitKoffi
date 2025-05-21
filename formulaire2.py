import tkinter as tk
from tkinter import ttk, messagebox

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Dashboard Admin")
fenetre.geometry("800x500")
fenetre.configure(bg="#f8f8f8")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f8f8f8", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))

# Header
header = ttk.Label(fenetre, text="Panneau d'administration", style="Title.TLabel")
header.pack(pady=20)

# Frame centrale avec colonnes
main_frame = tk.Frame(fenetre, bg="#f8f8f8")
main_frame.pack(pady=10, fill="both", expand=True)

# Liste des utilisateurs (exemple)
users_frame = ttk.LabelFrame(main_frame, text="Utilisateurs", padding=10)
users_frame.pack(side="left", fill="y", padx=20, pady=10)

user_listbox = tk.Listbox(users_frame, height=15, width=30)
user_listbox.pack()
for i in range(1, 11):
    user_listbox.insert(tk.END, f"Utilisateur {i}")

# Actions
action_frame = ttk.LabelFrame(main_frame, text="Actions rapides", padding=10)
action_frame.pack(side="right", fill="both", expand=True, padx=20, pady=10)

def ajouter_utilisateur():
    messagebox.showinfo("Ajouter", "Ajout d'un utilisateur (simulation)")

def supprimer_utilisateur():
    selection = user_listbox.curselection()
    if not selection:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un utilisateur.")
    else:
        user = user_listbox.get(selection[0])
        user_listbox.delete(selection[0])
        messagebox.showinfo("Suppression", f"{user} a été supprimé.")

ttk.Button(action_frame, text="Ajouter un utilisateur", command=ajouter_utilisateur).pack(pady=10, fill="x")
ttk.Button(action_frame, text="Supprimer l'utilisateur", command=supprimer_utilisateur).pack(pady=10, fill="x")
ttk.Button(action_frame, text="Exporter les données", command=lambda: messagebox.showinfo("Export", "Données exportées")).pack(pady=10, fill="x")

# Footer
footer = ttk.Label(fenetre, text="© 2025 MonAdminApp", font=("Segoe UI", 9))
footer.pack(pady=10)

fenetre.mainloop()
