# Dockerfile для веб-приложения

# Использование базового образа с Python
FROM --platform=linux/amd64 python:3.9

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

# Дефолтный порт, если не задан
ENV PORT 8000

# Команда по умолчанию для запуска приложения
CMD exec gunicorn -w 4 -b 0.0.0.0:${PORT} wsgi:app
