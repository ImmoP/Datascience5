# Verwende das offizielle Python-Image als Basis
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen (requirements.txt) in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Projektcode in das Arbeitsverzeichnis
COPY . .

# Starte die Anwendung
CMD [ "python", "app.py" ]
