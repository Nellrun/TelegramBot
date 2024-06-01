# Dockerfile для веб-приложения

# Использование базового образа с Python
FROM python:3.9-slim

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование requirements.txt в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего приложения в контейнер
COPY . .

# Копирование общих ресурсов
# COPY ../core /app/core

# Команда по умолчанию для запуска приложения
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
