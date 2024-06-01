# Makefile

VERSION := $(shell python -c "import uuid; print(uuid.uuid4())")

# Имя виртуального окружения
VENV := venv

# Определение путей к Python и pip в виртуальном окружении
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Пути до папок проектов
WEB_IMAGE := cr.yandex/crp8tu9klbd2oh20585s/template-web:$(VERSION)
BOT_IMAGE := cr.yandex/crp8tu9klbd2oh20585s/template-bot:$(VERSION)

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

build-web:
	docker build -t $(WEB_IMAGE) ./web
	docker push $(WEB_IMAGE)

build-bot:
	docker build -t $(BOT_IMAGE) ./bot
	docker push $(BOT_IMAGE)

# Запуск всего проекта
run: install run-web run-bot
