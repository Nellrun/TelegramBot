# Makefile

# Имя виртуального окружения
VENV := venv

# Определение путей к Python и pip в виртуальном окружении
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Определение пакетов
PACKAGES := flask telethon gunicorn python-dotenv

# Команды Makefile
.PHONY: all install clean run

# Установка виртуального окружения и зависимостей
install: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

# Запуск веб-приложения с использованием Gunicorn
run-web:
	$(VENV)/bin/gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app

# Запуск Telegram бота
run-bot:
	$(PYTHON) bot.py

# Удаление виртуального окружения и временных файлов
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Запуск всего проекта
run: install run-web run-bot
