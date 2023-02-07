# Nous allons utiliser l'image Python 3
FROM python:3

# Définissons le répertoire de travail 
WORKDIR /app

# Copions les dépendances dans le répertoire de travail
COPY requirements.txt .

# Installons les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copions le fichier de l'API dans le répertoire de travail
COPY test_api.py .

# Exposons le port 5000 pour notre API
EXPOSE 5000

# On lance la commande pour lancer l'API
CMD ["python", "test_api.py"]