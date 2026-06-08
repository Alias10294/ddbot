# Création du rag
# test git
# Imports
import json
from app.rag import configRag
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

def creer_rag():
    '''
    à partir des options de configRag, lit chaque URL, récupère le texte,
    le sépare en chunks avec texte, embedding, source et indice
    écrit le résultat dans un jsonl
    '''
    configRag.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(configRag.DATA_FILE, "w", encoding="utf-8") as f:
        pass

    liste_liens = configRag.liens_RAG
    nombre_liens = len(liste_liens)
    i=0
    for url in liste_liens:
        url_text = url_to_string_data(url)
        if url_text is None:
            # print(f"Erreur sur le chargement de l'url :{url}")
            i+=1
            continue
        
        chunks = text_to_chunks(url_text)
        embedded_chunks = model.encode([f"passage: {chunk}" for chunk in chunks], # préciser "passage" spécialité de multilingual-e5-large
                                       normalize_embeddings=True) # normaliser pour optimiser les calculs plus tard
        
        with open(configRag.DATA_FILE, "a", encoding="utf-8") as f:
            number_of_chunks=len(chunks)
            for c in range(number_of_chunks) :
                final_chunk ={
                    "url": url,
                    "chunk_index": c,
                    "content": chunks[c],
                    "embedding": embedded_chunks[c].tolist()
                }
                f.write(json.dumps(final_chunk, ensure_ascii=False) + "\n")

        i+=1
        # print(f"{i}/{nombre_liens} traité :{url}")