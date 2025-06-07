import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Cargar API Key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

# Función para obtener reseñas
def buscar_reviews():
    data_id = entry_data_id.get()
    if not data_id:
        messagebox.showwarning("Campo vacío", "Ingrese un data_id válido.")
        return

    params = {
        "engine": "google_maps_reviews",
        "data_id": data_id,
        "api_key": api_key,
        "hl": "es",
        "gl": "hn"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        reviews = results.get("reviews", [])

        if not reviews:
            messagebox.showinfo("Sin reseñas", "No se encontraron reseñas para este lugar.")
            return

        # Crear archivo CSV
        nombre_archivo = f"reviews_{data_id}.csv"
        with open(nombre_archivo, mode="w", newline='', encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Usuario", "Rating", "Fecha", "Comentario"])

            text_resultado.delete("1.0", tk.END)
            for r in reviews:
                usuario = r.get("user")
                rating = r.get("rating")
                fecha = r.get("date")
                comentario = r.get("snippet")

                text_resultado.insert(tk.END, f"👤 {usuario} | ⭐ {rating} | 🗓️ {fecha}\n📝 {comentario}\n{'-'*50}\n")
                writer.writerow([usuario, rating, fecha, comentario])

        messagebox.showinfo("Éxito", f"Reseñas guardadas en {nombre_archivo}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Interfaz con tkinter
root = tk.Tk()
root.title("CompetiTrack - Reseñas de Negocio")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Ingrese el data_id del negocio:").grid(column=0, row=0, sticky="w")
entry_data_id = ttk.Entry(frame, width=50)
entry_data_id.grid(column=1, row=0, padx=5)

btn_buscar = ttk.Button(frame, text="Buscar Reseñas", command=buscar_reviews)
btn_buscar.grid(column=2, row=0)

text_resultado = tk.Text(frame, width=100, height=25)
text_resultado.grid(column=0, row=1, columnspan=3, pady=10)

root.mainloop()
