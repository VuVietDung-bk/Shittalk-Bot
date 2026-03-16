import random
import discord
from discord import app_commands
from discord.ext import commands

SHITTALK_LINES = [
    "???",
    "bro what",
    "💀",
    "skill issue",
    "nah bro tripping",
    "Goo goo ga ga"
]

class ShittalkBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="g!",
            intents=intents,
            help_command=None,
        )
        # Xác suất ban đầu: 1/10
        self._chat_chance = 10

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced!")

    async def on_ready(self):
        print(f"{self.user} is online! 🌱")

    async def on_message(self, message: discord.Message):
        # Bỏ qua tin nhắn của chính bot
        if message.author == self.user:
            return

        # Thử xác suất hiện tại (1 / self._chat_chance)
        if random.randint(1, self._chat_chance) == 1:
            await message.channel.send(random.choice(SHITTALK_LINES))
            # Rerandom tỉ lệ: 1/1000 đến 1/10
            self._chat_chance = random.randint(10, 1000)

        await self.process_commands(message)