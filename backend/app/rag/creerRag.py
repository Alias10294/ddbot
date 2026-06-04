# Création du rag

# Imports
import json
import configRag
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("intfloat/multilingual-e5-large")

# Fonctions
def url_to_string_data(url):
    '''prend un url, retourne les données de la page en string'''
    # on essaie de charger la page
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None
    soup = BeautifulSoup(response.text, "html.parser")

    # enlever scripts/styles du html
    for tag in soup(["script", "style"]):
        tag.decompose()

    # ajouter des espaces et supprimer les espaces superflus
    text = soup.get_text(separator=" ", strip=True)
    return text

def text_to_chunks(text, chunk_size=configRag.CHUNK_SIZE, overlap=configRag.CHUNK_OVERLAP):
    ''' sépare un texte en liste de chunk de taille configRag.CHUNK_SIZE avec un overlap de configRag.CHUNK_OVERLAP'''
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

def main():
    for url in configRag.liens_RAG:
        url_text = url_to_string_data(url)
        if url_text is None:
            print(f"Erreur sur le chargement de l'url :{url}")
            continue
        
        print(f"Traitement de :{url}")
        chunks = text_to_chunks(url_text)
        embedded_chunks = model.encode([f"passage: {chunk}" for chunk in chunks]) # préciser "passage" spécialité de multilingual-e5-large
        
        with open(configRag.DATA_FILE, "a", encoding="utf-8") as f:
            number_of_chunks=len(chunks)
            for i in range(number_of_chunks) :
                final_chunk ={
                    "url": url,
                    "chunk_index": i,
                    "content": chunks[i],
                    "embedding": embedded_chunks[i].tolist()
                }
                f.write(json.dumps(final_chunk, ensure_ascii=False) + "\n")

main()