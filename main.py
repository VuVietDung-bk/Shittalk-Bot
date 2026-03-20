import os
import logging
import webserver

from dotenv import load_dotenv

from bot import ShittalkBot

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")

    if not TOKEN:
        print("⚠️ Please set DISCORD_BOT_TOKEN environment variable")
        print("Example: export DISCORD_BOT_TOKEN='your_token_here'")
    else:
        # Debug: kiểm tra token
        print(f"Token length: {len(TOKEN)}")
        print(f"Token starts with: {TOKEN[:10]}...")
        print(f"Token ends with: ...{TOKEN[-10:]}")
        TOKEN = TOKEN.strip()  # Loại bỏ khoảng trắng đầu/cuối
        handler = logging.FileHandler(
            filename="discord.log", encoding="utf-8", mode="w"
        )
        bot = ShittalkBot()
        webserver.keep_alive()
        bot.run(TOKEN, log_handler=handler, log_level=logging.INFO)
