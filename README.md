# Telegram Bot Template with Web App

This repository contains a template for building Telegram bots using Telethon and a web application using Flask. The bot sends a button that opens the web application.

## Features

- **Telegram Bot**: Built using Telethon, capable of responding to commands and sending interactive buttons.
- **Web Application**: Simple web app built using Flask, easily extendable for more complex functionality.
- **Makefile**: Automates setup, running, and cleaning tasks.

## Prerequisites

- Python 3.x
- Git

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Nellrun/TelegramBot.git
    cd TelegramBot
    ```

2. Create a virtual environment and install the dependencies:

    ```bash
    make install
    ```

## Configuration

1. Get your API ID and API Hash from [my.telegram.org](https://my.telegram.org).
2. Create a new bot and get the bot token from [BotFather](https://t.me/BotFather).
3. Update `bot.py` with your API ID, API Hash, and Bot Token:

    ```python
    api_id = 'YOUR_API_ID'
    api_hash = 'YOUR_API_HASH'
    bot_token = 'YOUR_BOT_TOKEN'
    ```

## Usage

### Running the Web Application

To run the web application using Gunicorn:

```bash
make run-web
```

### Running the Telegram Bot

To run the Telegram bot:

```bash
make run-bot
```

### Running Both Web Application and Bot

To run both the web application and the Telegram bot:

```bash
make run
```

### Cleaning Up

To remove the virtual environment and temporary files:

```bash
make clean
```

## Template Usage

This repository is intended to be a starting point for creating new Telegram bots. You can clone this repository and modify the files as needed to develop your own bots. The template includes a basic setup for a bot that sends a button linking to a web application, but it can be easily extended with additional functionality.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

