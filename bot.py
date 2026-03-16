import random
import discord
from discord.ext import commands

SHITTALK_LINES = [
    "chao cau chu",
    "goo goo ga ga",
    "cau chu thang lon roi",
    "t cho may noi chua",
    "t cho m cam than chua",
    "mambo mambo omatsuri mambo",
    "gogetajob",
    "t giet",
    "me long se khoc mat",
    "stfu nigga",
    "ngam mom vao, thang hai nua mua",
    "Nguyen Ha Dong lam duoc thi toi cung lam duoc",
    "can nha o pho co Ha Noi"
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
        # Đếm số lần fail liên tiếp
        self._fail_count = 0

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced!")

    async def on_ready(self):
        print(f"{self.user} is online!")

    async def on_message(self, message: discord.Message):
        # Bỏ qua tin nhắn của chính bot
        if message.author == self.user:
            return

        # Sau 97 lần fail, chắc chắn thành công
        if self._fail_count >= 97:
            await message.channel.send(random.choice(SHITTALK_LINES))
            self._chat_chance = random.randint(20, 200)
            self._fail_count = 0
        # Thử xác suất hiện tại (1 / self._chat_chance)
        elif random.randint(1, self._chat_chance) == 1:
            await message.channel.send(random.choice(SHITTALK_LINES))
            # Rerandom tỉ lệ
            self._chat_chance = random.randint(20, 200)
            self._fail_count = 0
        else:
            self._fail_count += 1

        await self.process_commands(message)