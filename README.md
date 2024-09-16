# Discord Random Link API Bot

A Discord bot that responds to the `/gameapi` slash command by retrieving a random link from a local `websiteapi.txt` file. This is perfect for game servers or any Discord server where you'd like to deliver random content or pages to users.

## Features

- **Random Link Selection**: Fetches a random URL from a text file and sends it in Discord chat.
- **Customizable Links**: Easily update the `websiteapi.txt` file to include your own list of URLs.
- **Slash Commands**: Utilizes Discord's modern slash commands for clean and easy interaction.

## Setup Instructions

Follow these steps to set up the bot on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/discord-random-link-bot.git
cd discord-random-link-bot
```

### 2. Install Dependencies

Make sure you have Python installed (version 3.8 or higher). Then, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

The required packages include:
- `discord.py`
- `python-dotenv`

### 3. Create the `.env` File

In the root directory, create a `.env` file to store your Discord bot token:

```
DISCORD_TOKEN=your-discord-bot-token
```

Replace `your-discord-bot-token` with the token for your Discord bot. You can get this token from the [Discord Developer Portal](https://discord.com/developers/applications).

### 4. Add Links to the `websiteapi.txt` File

In the `assets/` folder, create or update the `websiteapi.txt` file. Add each URL you want to include on a new line. For example:

```
https://example.com/page1
https://example.com/page2
https://example.com/page3
```

### 5. Run the Bot

Once everything is set up, you can run the bot with:

```bash
python main.py
```

If successful, you should see a message in the terminal that the bot is logged in and ready to respond.

## Usage

To use the bot in your Discord server:

1. Invite the bot to your server using the bot invite link from the [Discord Developer Portal](https://discord.com/developers/applications).
2. In any channel, type `/gameapi`. The bot will respond with a random link from the `websiteapi.txt` file.

## File Structure

```text
discord-bot/
│
├── assets/
│   └── websiteapi.txt        # The file containing the list of URLs (one per line)
├── commands/
│   └── gameapi.py            # Cog that defines the /gameapi command
├── .env                      # Stores your Discord bot token
├── main.py                   # The entry point of the bot
├── requirements.txt          # List of dependencies for the project
└── README.md                 # Project documentation
```

### Example of `websiteapi.txt`

```text
https://example1.com
https://example2.com
https://example3.com
```

## Contributions

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and submit a pull request.

### To Contribute:

1. Fork the project
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit the changes (`git commit -m 'Add new feature'`)
5. Push the branch (`git push origin feature-branch`)
6. Open a pull request

