# DDBot: Le Chatbot Interactif (que pour les utilisateurs Linux)
## Installation
### Exigences
L'application DDBot est contenerisée avec Docker, donc pour utiliser l'application, il vous faudra donc Docker Desktop.
Elle utilise également Ollama et Langflow pour son modèle

### Procédé d'installation
Pour récupérer l'application, placez vous dans le dossier de votre choix et clonez le repository:
```text
> git clone https://github.com/Alias10294/ddbot
```
Ensuite, il suffira de lancer le conteneur avec la commande:
```text
> docker compose up
```

L'application sera ensuite disponible à l'adresse:
```text
http://localhost:5173
```