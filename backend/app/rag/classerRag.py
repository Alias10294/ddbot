from app.rag import configRag
import numpy as np
import json
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("intfloat/multilingual-e5-large")

# score(n)=λ⋅sim(q,n)−(1−λ)⋅k∈selectedmax​sim(n,k)
# score(i)=λ⋅sim(q,i)−(1−λ)⋅j∈selectedmax​sim(i,j)
# mmr incrémental


def mmr_indice(query_vec, doc_vecs, lambda_, top_k):
    # Initialisation des données
    candidates = set(range(len(doc_vecs)))                               # tableau temporaire des embeddings
    pertinence = (query_vec @ doc_vecs.T).ravel()                        # tableau de la pertinence entre les embedding et la question
    selected = []                                                        # indices des résultats sélectionnés

    for _ in range(top_k):
        mmr_scores = []

        for n in candidates:
            if not selected:
                similarite = 0
            else:
                similarite = max(doc_vecs[n] @ doc_vecs[k] for k in selected)

            score = lambda_ * pertinence[n] - (1 - lambda_) * similarite
            mmr_scores.append((score, n))

        _, best = max(mmr_scores)
        selected.append(best)
        candidates.remove(best)

    return selected


def selectionner_chunk(query):
    '''prend en paramètre la question en string
    retourne les k meilleurs chunks'''

    # On récupère les embeddings
    embedded_chunks = []
    with open(configRag.DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            embedded_chunks.append(d["embedding"]) 

    # On sélectionne les chunks en comparant les embeddings
    query_vec = model.encode(f"query: {query}", normalize_embeddings=True) # préciser "query" spécialité de multilingual-e5-large
    query_vec = np.asarray(query_vec).reshape(1, -1)
    selected = mmr_indice(query_vec, doc_vecs=np.array(embedded_chunks), lambda_=configRag.LAMBDA, top_k=configRag.NUMBER_OF_CHUNK_SELECTED)

    # On charge les cunks sélectionnés
    results = []
    with open(configRag.DATA_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i in selected:
                results.append(json.loads(line))
    return(results)

def test():
    question = "comment assurer la sécurité informatique d'un ordinateur ?"
    selection=selectionner_chunk(question)
    i=0
    for s in selection:
        i+=1
        print(f"\nChunk {i} sur {configRag.NUMBER_OF_CHUNK_SELECTED} ---------------------------------------")
        print(s["url"])
        print(s["content"])

if __name__ == "__main__":
    test()