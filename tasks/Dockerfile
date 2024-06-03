# Используем официальный образ Python
FROM --platform=linux/amd64 python:3.9

# Установка зависимостей
RUN apt-get update && apt-get install -y cron


# Устанавливаем рабочую директорию
WORKDIR /app

# Копирование requirements.txt в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего приложения в контейнер
COPY . .

# Копирование общих ресурсов
# COPY ../core /app/core

# Копируем скрипт и файл crontab в рабочую директорию
COPY crontab /etc/cron.d/my-cron-tasks

# Настройка прав для файла crontab
RUN chmod 0644 /etc/cron.d/my-cron-tasks

# Запуск cron
RUN crontab /etc/cron.d/my-cron-tasks
RUN touch /var/log/cron.log

# Команда для запуска cron в фоновом режиме
CMD cron && tail -f /var/log/cron.log
