# DCvoice24-7
This is a simple Discord bot created using Discord.py.

Prerequisites
Python 3.6 or higher
Discord.py
Discord Bot Token
Getting Started
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

Commands
join - Makes the bot join the user's voice channel
ping - Returns the bot's latency in milliseconds
mc <voice_channel_id> - Shows the number of human and bot users in the specified voice channel
Acknowledgments
Discord.py Documentation
Python Discord Bot Tutorial
