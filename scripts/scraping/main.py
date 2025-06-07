import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

# Función para buscar negocios
def buscar_negocios():
    query = entry_busqueda.get()
    if not query:
        messagebox.showwarning("Campo vacío", "Ingrese una búsqueda.")
        return

    params = {
        "engine": "google_maps",
        "q": query,
        "ll": "@15.514920,-87.992271,14z",  # Coordenadas SPS
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        lugares = results.get("local_results", [])

        # Crear CSV
        nombre_archivo = f"resultados_{query}.csv"
        with open(nombre_archivo, mode="w", newline='', encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre", "Rating", "Dirección", "Teléfono", "Data ID"])

            text_resultado.delete("1.0", tk.END)
            for place in lugares:
                nombre = place.get("title")
                rating = place.get("rating")
                direccion = place.get("address")
                telefono = place.get("phone")
                data_id = place.get("data_id")

                # Escribir en el TextBox
                text_resultado.insert(tk.END, f"🏪 {nombre}\n")
                text_resultado.insert(tk.END, f"⭐ Rating: {rating}\n")
                text_resultado.insert(tk.END, f"📍 Dirección: {direccion}\n")
                text_resultado.insert(tk.END, f"📞 Teléfono: {telefono}\n")
                text_resultado.insert(tk.END, f"🆔 data_id: {data_id}\n")
                text_resultado.insert(tk.END, "-" * 40 + "\n")

                # Escribir en CSV
                writer.writerow([nombre, rating, direccion, telefono, data_id])

        messagebox.showinfo("Éxito", f"Resultados guardados en {nombre_archivo}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz con tkinter
root = tk.Tk()
root.title("CompetiTrack - Búsqueda en Google Maps")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Buscar negocios:").grid(column=0, row=0, sticky="w")
entry_busqueda = ttk.Entry(frame, width=40)
entry_busqueda.grid(column=1, row=0, padx=5)

btn_buscar = ttk.Button(frame, text="Buscar", command=buscar_negocios)
btn_buscar.grid(column=2, row=0)

text_resultado = tk.Text(frame, width=80, height=20)
text_resultado.grid(column=0, row=1, columnspan=3, pady=10)

root.mainloop()
