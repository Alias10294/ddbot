# DDBot: Le Chatbot Interactif (que pour les utilisateurs Linux)
## Installation
### Exigences
L'application DDBot est contenerisée avec Docker, donc pour utiliser l'application, il vous faudra donc Docker Desktop.
Elle utilise également Ollama et Langflow pour son modèle, donc créer un compte Ollama sera nécessaire.

### Procédé d'installation
Pour récupérer l'application, placez vous dans le dossier de votre choix et clonez le repository:
```text
> git clone https://github.com/Alias10294/ddbot
```
Ensuite, il suffira de lancer le conteneur avec la commande:
```text
> docker compose up
```
L'application fonctionne grâce à un modèle performant du cloud de Ollama, donc il faudra se connecter:
```text
> docker exec -it ddbot-ollama ollama signin
```
De là, il faudra suivre le lien affiché et se connecter.

Une fois ces étapes passées, l'application devrait être pleinement fonctionnelle et sera disponible à votre adresse:
```text
http://localhost:5173
```

### Disclaimer
Chaque service de l'application, particulièrement Langflow, peut prendre plusieurs minutes à être opérationnel. Avant cela, l'interface graphique sera disponible, mais l'agent ne sera pas prêt.