# Shittalk Bot

A Discord bot that randomly replies to messages with funny/sarcastic one-liners.

## Features

- **Random replies** - Bot replies to messages with a configurable probability
- **Dynamic difficulty** - Probability changes after each reply to keep things unpredictable
- **Guaranteed message** - After 97 consecutive failures, the bot is guaranteed to reply on the next message
- **Customizable lines** - Easily add or modify the list of phrases the bot can say

## How It Works

1. Initial chance: **1/10** - For every 10 messages, roughly 1 will trigger a bot response
2. After replying, the probability is re-randomized to somewhere between **1/20 and 1/200**
3. If the bot fails to reply 97 times in a row, it is **guaranteed** to reply on the 98th message
4. The failure counter resets when the bot successfully replies

## Configuration

Edit the `SHITTALK_LINES` list in `bot.py` to add or remove phrases:

```python
SHITTALK_LINES = [
    "your custom line here",
    "another funny response",
    # ... add more lines
]
```

## Prerequisites

- Python 3.8 or higher
- `discord.py` library (2.0+)
- `python-dotenv` for environment variables

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd shittalk-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   DISCORD_BOT_TOKEN=your_bot_token_here
   ```

4. Get your bot token:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Navigate to "Bot" section and create a bot
   - Copy the token and paste it in `.env`

5. Invite the bot to your server:
   - In Developer Portal, go to OAuth2 > URL Generator
   - Select scopes: `bot`
   - Select permissions: `Send Messages`
   - Copy the generated URL and open it in your browser to invite the bot

## Running the Bot

```bash
python3 main.py
```

The bot will start and be ready to respond to messages.

## Deploying on Render

### Setup Instructions

1. Push your code to GitHub
2. Go to [Render.com](https://render.com/) and create a new Web Service
3. Connect your GitHub repository
4. Configure the service:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `python3 main.py`
   - **Environment Variables**: Add `DISCORD_BOT_TOKEN` with your bot token value
5. Deploy!

## File Structure

```
shittalk-bot/
├── bot.py              # Main bot class
├── main.py             # Bot entry point
├── webserver.py        # Flask server for keeping bot alive
├── .env                # Environment variables (create this)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Troubleshooting

### Bot doesn't respond
- Ensure `DISCORD_BOT_TOKEN` is set correctly in `.env`
- Check that the bot has permission to send messages in the channel
- Verify the bot has the "Send Messages" permission

### Bot not starting
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check for syntax errors in `SHITTALK_LINES`
- Verify Python version is 3.8 or higher: `python3 --version`

## License

This project is provided as-is for personal use.