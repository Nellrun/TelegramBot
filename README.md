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

2. Create a `.env` file in the root directory and add your API ID, API Hash, and Bot Token:

    ```dotenv
    API_ID=your_api_id
    API_HASH=your_api_hash
    BOT_TOKEN=your_bot_token
    ```


## Configuration

1. Get your API ID and API Hash from [my.telegram.org](https://my.telegram.org).
2. Create a new bot and get the bot token from [BotFather](https://t.me/BotFather).
3. Update `bot.py` with your API ID, API Hash, and Bot Token:

    ```python
    api_id = 'YOUR_API_ID'
    api_hash = 'YOUR_API_HASH'
    bot_token = 'YOUR_BOT_TOKEN'
    WEB_URL = 'http://127.0.0.1:8000/'
    ```

## Usage

### Running Both Web Application and Bot

To run both the web application and the Telegram bot:

```bash
docker-compose up --build
```

## Template Usage

This repository is intended to be a starting point for creating new Telegram bots. You can clone this repository and modify the files as needed to develop your own bots. The template includes a basic setup for a bot that sends a button linking to a web application, but it can be easily extended with additional functionality.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

