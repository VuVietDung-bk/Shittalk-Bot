import random
import discord
import traceback
from discord import app_commands
from discord.ext import commands

SHITTALK_LINES = {
    "chao cau chu": "<:hlgotnonetosay:1402967694470418594>",
    "goo goo ga ga": "<:hlgotnonetosay:1402967694470418594>",
    "cau chu thang lon roi": "<:hlgotnonetosay:1402967694470418594>",
    "t cho may noi chua": "<:gotnonetocook:1409548321395183678>",
    "t cho m cam than chua": "<:gotnonetocook:1409548321395183678>",
    "mambo mambo omatsuri mambo": "<:hlgotnonetosay:1402967694470418594>",
    "gogetajob": "<:hlgotnonetosay:1402967694470418594>",
    "t giet": "<:gotnonetocook:1409548321395183678>",
    "me long se khoc mat": "<:hlgotnonetosay:1402967694470418594>",
    "stfu nigg-": "<:fire_speaking:1477284820844544122>",
    "ngam mom vao, thang hai nua mua": "<:gotnonetocook:1409548321395183678>",
    "Nguyen Ha Dong lam duoc thi toi cung lam duoc": "<:hlgotnonetosay:1402967694470418594>",
    "can nha o pho co Ha Noi": "<:hlgotnonetosay:1402967694470418594>",
    "hoi AI di em": "<:hlgotnonetosay:1402967694470418594>",
    "bt sao ragebait toi manh k vi toi toan noi thang tim den ng khac ra": "<:hlgotnonetosay:1402967694470418594>",
    "co dien ton trong 💔": "<:hlgotnonetosay:1402967694470418594>",
    "chia kho thap, cut nay tieu hoi tat": "<:hlgotnonetosay:1402967694470418594>",
    "kien thuc bong tinh anh": "<:hlgotnonetosay:1402967694470418594>",
    "donkey enough to make a joke like that": "<:gotnonetocook:1409548321395183678>",
    "mdf": "<:gotnonetocook:1409548321395183678>",
    "luck top 0": "<:hlgotnonetosay:1402967694470418594>",
    "thang nhan phia tren la gay 🏳️‍🌈": "<:hlgotnonetosay:1402967694470418594>",
    "Hắn sẽ gây ra những hậu quả \"kinh khủng\" cho cả bạn và lũ thây ma!": "<:fire_speaking:1477284820844544122>",
    "tao del chua may ra": "<:hlgotnonetosay:1402967694470418594>",
    "co cut": "<:gotnonetocook:1409548321395183678>",
    "toi di roi mn len pho lang thay cho toi nhe, co gang thay doi discord LKT, de LKT khong con tinh trang nhu bay h nua": "<:arisu_cry:1332925707742875690>",
    "co ai binh thuong de biet viec bi chui thi co la joke no cung ko hai k": "<:arisu_cry:1332925707742875690>",
    "IQ k thap den muc k nhan ra no dang nch voi ai": "<:hlgotnonetosay:1402967694470418594>",
    "noi thu a dang de ton trong di a": "<:hlgotnonetosay:1402967694470418594>",
    "e ko xem nguoi chet la nguoi song dau a": "<:hlgotnonetosay:1402967694470418594>",
    "donate cho t 200k di dang doi": "😝",
    "chac chi la con gio": "<:hlgotnonetosay:1402967694470418594>",
    "đừng làm t ngứa mắt nữa": "<:akiehahahahahahahahhhahahahahaha:1487298163999117342>",
    "câm": "<:akiehahahahahahahahhhahahahahaha:1487298163999117342>",
    "dám làm ko dám nhận nhưng khác vs t ở chỗ shion đổ cho ng khác": "<:akiehahahahahahahahhhahahahahaha:1487298163999117342>",
    "Luck does not exist. Things happen according to The Lord Jesus's plan and doesn't happen based on chances.": "<:fire_speaking:1477284820844544122>",
    "choi td di e": "<:hlgotnonetosay:1402967694470418594>",
}

class ShittalkBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="nl!",
            intents=intents,
            help_command=None,
        )
        # Xác suất ban đầu: 1/10
        self._chat_chance = 10
        # Đếm số lần fail liên tiếp
        self._fail_count = 0
        # Danh sách channel ID được phép
        self._allowed_channels: set[int] = set()
        # Danh sách user ID bị bỏ qua
        self._excluded_users: set[int] = set()
        # Owner ID
        self._owner_id: int | None = None
        # Flag để tracking xem đã claim owner chưa
        self._owner_claimed = False

    async def setup_hook(self):
        self.tree.add_command(_claim_owner)
        self.tree.add_command(_add_channel)
        self.tree.add_command(_remove_channel)
        self.tree.add_command(_exclude_myself)
        self.tree.add_command(_exclude_user)
        self.tree.add_command(_current_stat)
        
        # Thêm error handler cho slash commands
        @self.tree.error
        async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
            print(f"❌ Slash command error: {error}")
            if not interaction.response.is_done():
                await interaction.response.send_message(
                    f"⚠️ Có lỗi xảy ra: {str(error)}", 
                    ephemeral=True
                )
        
        await self.tree.sync()
        print("Slash commands synced!")

    async def on_ready(self):
        print(f"{self.user} is online!")

    async def _send_shittalk(self, channel: discord.TextChannel):
        """Gửi tin nhắn random + 1/2 tỉ lệ gửi thêm emoji"""
        try:
            line = random.choice(list(SHITTALK_LINES.keys()))
            emoji = SHITTALK_LINES[line]
            await channel.send(line)
            # 1/2 tỉ lệ gửi thêm emoji
            if random.randint(1, 2) == 1:
                await channel.send(emoji)
        except discord.HTTPException as e:
            print(f"⚠️ Failed to send shittalk: {e}")
        except Exception as e:
            print(f"❌ Unexpected error in _send_shittalk: {e}")

    async def on_message(self, message: discord.Message):
        try:
            # Bỏ qua tin nhắn của chính bot
            if message.author == self.user:
                return

            # Bỏ qua nếu user nằm trong danh sách excluded
            if message.author.id in self._excluded_users:
                return

            # Bỏ qua nếu channel không nằm trong danh sách allowed
            if message.channel.id not in self._allowed_channels:
                return

            # Sau 97 lần fail, chắc chắn thành công
            if self._fail_count >= 97:
                await self._send_shittalk(message.channel)
                self._chat_chance = random.randint(20, 200)
                self._fail_count = 0
            # Thử xác suất hiện tại (1 / self._chat_chance)
            elif random.randint(1, self._chat_chance) == 1:
                await self._send_shittalk(message.channel)
                # Rerandom tỉ lệ
                self._chat_chance = random.randint(20, 200)
                self._fail_count = 0
            else:
                self._fail_count += 1

            await self.process_commands(message)
        except Exception as e:
            print(f"❌ Error in on_message: {e}")
            traceback.print_exc()


# ── Slash commands ─────────────────────────────────────────────────────


@app_commands.command(
    name="addchannel",
    description="Thêm channel vào danh sách bot sẽ reply.",
)
@app_commands.describe(channel="Channel cần thêm (mặc định: channel hiện tại)")
async def _add_channel(interaction: discord.Interaction, channel: discord.TextChannel = None):
    bot: ShittalkBot = interaction.client
    channel_id = channel.id if channel else interaction.channel_id
    if channel_id in bot._allowed_channels:
        await interaction.response.send_message(
            f"<#{channel_id}> đã có trong danh sách rồi.", ephemeral=True
        )
    else:
        bot._allowed_channels.add(channel_id)
        await interaction.response.send_message(
            f"✅ Đã thêm <#{channel_id}> vào danh sách.", ephemeral=True
        )


@app_commands.command(
    name="removechannel",
    description="Xóa channel khỏi danh sách bot sẽ reply.",
)
@app_commands.describe(channel="Channel cần xóa (mặc định: channel hiện tại)")
async def _remove_channel(interaction: discord.Interaction, channel: discord.TextChannel = None):
    bot: ShittalkBot = interaction.client
    # Kiểm tra nếu chỉ owner mới được gọi
    if bot._owner_id is not None and interaction.user.id != bot._owner_id:
        await interaction.response.send_message(
            "❌ Chỉ owner mới có thể xóa channel.", ephemeral=True
        )
        return
    
    channel_id = channel.id if channel else interaction.channel_id
    if channel_id not in bot._allowed_channels:
        await interaction.response.send_message(
            f"<#{channel_id}> không có trong danh sách.", ephemeral=True
        )
    else:
        bot._allowed_channels.discard(channel_id)
        await interaction.response.send_message(
            f"✅ Đã xóa <#{channel_id}> khỏi danh sách.", ephemeral=True
        )


@app_commands.command(
    name="excludemyself",
    description="Thêm bản thân vào danh sách bỏ qua (bot sẽ không tính tin nhắn của bạn).",
)
async def _exclude_myself(interaction: discord.Interaction):
    bot: ShittalkBot = interaction.client
    user_id = interaction.user.id
    if user_id in bot._excluded_users:
        # Toggle: nếu đã exclude thì bỏ exclude
        bot._excluded_users.discard(user_id)
        await interaction.response.send_message(
            f"✅ Bạn đã được bỏ khỏi danh sách loại trừ. Bot sẽ tính tin nhắn của bạn.",
            ephemeral=True,
        )
    else:
        bot._excluded_users.add(user_id)
        await interaction.response.send_message(
            f"✅ Bạn đã được thêm vào danh sách loại trừ. Bot sẽ bỏ qua tin nhắn của bạn.",
            ephemeral=True,
        )


@app_commands.command(
    name="claimowner",
    description="Claim owner bot (chỉ được gọi một lần).",
)
async def _claim_owner(interaction: discord.Interaction):
    bot: ShittalkBot = interaction.client
    if bot._owner_claimed:
        await interaction.response.send_message(
            "❌ Owner đã được claim rồi. Không thể claim lệnh.", ephemeral=True
        )
    else:
        bot._owner_id = interaction.user.id
        bot._owner_claimed = True
        await interaction.response.send_message(
            f"✅ <@{interaction.user.id}> đã become owner của bot!",
            ephemeral=True,
        )


@app_commands.command(
    name="excludeuser",
    description="Exclude hoặc include user (chỉ owner mới được gọi).",
)
@app_commands.describe(user="User ID cần exclude/include")
async def _exclude_user(interaction: discord.Interaction, user: discord.User):
    bot: ShittalkBot = interaction.client
    # Kiểm tra nếu chỉ owner mới được gọi
    if bot._owner_id is not None and interaction.user.id != bot._owner_id:
        await interaction.response.send_message(
            "❌ Chỉ owner mới có thể exclude user.", ephemeral=True
        )
        return
    
    if user.id in bot._excluded_users:
        # Toggle: nếu đã exclude thì bỏ exclude
        bot._excluded_users.discard(user.id)
        await interaction.response.send_message(
            f"✅ <@{user.id}> đã được bỏ khỏi danh sách loại trừ. Bot sẽ tính tin nhắn của họ.",
            ephemeral=True,
        )
    else:
        bot._excluded_users.add(user.id)
        await interaction.response.send_message(
            f"✅ <@{user.id}> đã được thêm vào danh sách loại trừ. Bot sẽ bỏ qua tin nhắn của họ.",
            ephemeral=True,
        )


@app_commands.command(
    name="currentstat",
    description="Hiển thị số lần fail liên tiếp và tỉ lệ hiện tại.",
)
async def _current_stat(interaction: discord.Interaction):
    bot: ShittalkBot = interaction.client
    await interaction.response.send_message(
        f"📊 **Thống kê hiện tại**\n"
        f"• Số lần fail liên tiếp: **{bot._fail_count}**/97\n"
        f"• Tỉ lệ hiện tại: **1/{bot._chat_chance}**",
        ephemeral=True,
    )