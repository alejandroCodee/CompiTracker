import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Cargar la API Key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

# Parámetros de búsqueda en Google Maps (San Pedro Sula)
params = {
    "engine": "google_maps",
    "q": "Pizza",
    "ll": "@15.514920,-87.992271,14z",  # Coordenadas de SPS
    "api_key": api_key
}

# Ejecutar búsqueda
search = GoogleSearch(params)
results = search.get_dict()

# Imprimir resultados de forma legible
print("\n📍 Negocios encontrados:\n")

for place in results.get("local_results", []):
    nombre = place.get("title")
    rating = place.get("rating")
    direccion = place.get("address")
    telefono = place.get("phone")
    data_id = place.get("data_id")
    
    print(f"🏪 {nombre}")
    print(f"⭐ Rating: {rating}")
    print(f"📍 Dirección: {direccion}")
    print(f"📞 Teléfono: {telefono}")
    print(f"🆔 data_id: {data_id}")
    print("-" * 40)
