# Dockerfile для бота

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

# Команда по умолчанию для запуска бота
CMD python bot.py
