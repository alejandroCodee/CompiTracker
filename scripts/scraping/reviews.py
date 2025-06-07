import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Cargar la API Key
load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

# Parámetros de búsqueda en Google Maps (San Pedro Sula)
params = {
    "engine": "google_maps_reviews",
    "type": "search",
    "data_id": "0x8f6645673ad50485:0xdccc11eedcbc8b22",  # ID de un lugar específico
    "api_key": api_key
}

# Ejecutar búsqueda
search = GoogleSearch(params)
results = search.get_dict()

for review in results.get("reviews", []):
    author = review.get("user")
    rating = review.get("rating")
    date = review.get("date")
    text = review.get("snippet")
    
    print(f"👤 {author} | ⭐ {rating} | 🗓️ {date}\n📝 {text}\n{'-'*50}")