FROM python:3.10-slim

# permet d’avoir les logs en “temps réel”
ENV PYTHONUNBUFFERED 1

# Installer les dépendances système dont on aura besoin
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

# Ouvrir le port 8000
EXPOSE 8000

# Démarrage
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

