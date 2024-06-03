# Telegram Bot Template with Flask and Telethon

This repository provides a template for creating a Telegram bot using Python, Flask, and Telethon. The project is structured to facilitate development, testing, and deployment using Docker.

## Project Structure

- **web/**: Contains the Flask backend for the mini app. 
- **bot/**: Contains the logic for bot commands written with Telethon.
- **tasks/**: Contains background cron tasks.
- **core/**: Contains common Python modules used across the project.
- **docker-compose.yml**: Docker Compose configuration for building and running all containers.

### Common Modules

The `core` directory contains common Python modules used across the project. Ensure any shared logic or utilities are placed here for reusability.

## Prerequisites

- Python 3.x
- Docker
- Docker-compose

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
    WEB_URL=your_url_address
    ```


## Configuration

1. Get your API ID and API Hash from [my.telegram.org](https://my.telegram.org).
2. Create a new bot and get the bot token from [BotFather](https://t.me/BotFather).
3. Update `.env` with your API ID, API Hash, and Bot Token:

    ```python
    api_id = 'YOUR_API_ID'
    api_hash = 'YOUR_API_HASH'
    bot_token = 'YOUR_BOT_TOKEN'
    WEB_URL = 'http://127.0.0.1:8000/'
    ```

### Using Docker Compose

The project includes a `docker-compose.yml` file to streamline the process of building and running all components together.

To build and start all services:

```bash
docker-compose up --build
```

To stop the services:

```bash
docker-compose down
```

## Template Usage

This repository is intended to be a starting point for creating new Telegram bots. You can clone this repository and modify the files as needed to develop your own bots. The template includes a basic setup for a bot that sends a button linking to a web application, but it can be easily extended with additional functionality.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
