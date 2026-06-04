from pathlib import Path

# Chemin vers le jsonl dans lequel est stocké le rag
BACKEND_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BACKEND_DIR / "data" / "chunks.jsonl"

# 
liens_RAG = [
    "https://numerique.uphf.fr/organisation/s%C3%A9curit%C3%A9%20des%20syst%C3%A8mes%20d%27information",
    "https://www.info.gouv.fr/risques",
    "https://cyber.gouv.fr/"
]

# Paramètres pour les chunks
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150