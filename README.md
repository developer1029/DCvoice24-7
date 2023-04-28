# DCvoice24-7

This is a simple Discord bot written in Python using the `discord.py` library. The bot can be used to connect to a voice channel, display the number of humans and bots in a voice channel, and check the bot's latency.

## Setup

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
4. Copy the bot token and add it to the `TOKEN` variable in the `bot.py` file.
5. Run the bot by executing `python bot.py`.

## Usage

The bot has the following commands:

- `..join`: Joins the voice channel of the user who sent the command.
- `..ping`: Checks the latency of the bot.
- `..mc <channel_id>`: Displays the number of humans and bots in the specified voice channel.









## Prerequisites

- Python 3.6 or higher
- Discord.py
- Discord Bot Token

## Getting Started

To get started, make sure you have Python 3.6 or higher installed on your computer. Clone this repository to your local machine, navigate to the project directory and install the required packages using pip:

```py
pip install -r requirements.txt
```
To run the bot, you need to create a Discord bot and obtain a token. You can follow the instructions on Discord Developer Portal to create a bot and get its token.

Then, replace TOKEN in the code with your bot's token.


```
TOKEN = "YOUR_BOT_TOKEN_HERE"
```
You can customize the bot prefix by changing the PREFIX variable:

```
PREFIX = '..'
```

```
python bot.py
```

## Commands

- join - Makes the bot join the user's voice channel
- ping - Returns the bot's latency in milliseconds
- mc <voice_channel_id> - Shows the number of human and bot users in the specified voice channel

## Acknowledgments
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).
