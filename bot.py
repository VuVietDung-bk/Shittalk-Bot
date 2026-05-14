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
    "toi di roi mn len pho lang thay cho toi nhe, co gang thay doi discord LKT, de LKT khong con tinh trang nhu bay h nua": "<:arisu_cry:1497613253465866360>",
    "co ai binh thuong de biet viec bi chui thi co la joke no cung ko hai k": "<:arisu_cry:1497613253465866360>",
    "IQ k thap den muc k nhan ra no dang nch voi ai": "<:hlgotnonetosay:1402967694470418594>",
    "noi thu a dang de ton trong di a": "<:hlgotnonetosay:1402967694470418594>",
    "e ko xem nguoi chet la nguoi song dau a": "<:hlgotnonetosay:1402967694470418594>",
    "donate cho t 200k di dang doi": "😝",
    "chac chi la con gio": "<:hlgotnonetosay:1402967694470418594>",
    "đừng làm t ngứa mắt nữa": "<:akiethumb:1488224506714525747>",
    "câm": "<:akiethumb:1488224506714525747>",
    "dám làm ko dám nhận nhưng khác vs t ở chỗ shion đổ cho ng khác": "<:akiethumb:1488224506714525747>",
    "Luck does not exist. Things happen according to The Lord Jesus's plan and doesn't happen based on chances.": "<:fire_speaking:1477284820844544122>",
    "choi td di e": "<:hlgotnonetosay:1402967694470418594>",
    "dung lai lam on": "<:crano:1482747125736411407>",
    "lucacucu": "<:hlgotnonetosay:1402967694470418594>",
    "san nha phuc co thich choi bo lu a chi": "<:fire_speaking:1477284820844544122>",
    "neu ban doi xu voi mot con cho nhu mot con nguoi, no se doi xu voi ban nhu mot con cho": "<:hlgotnonetosay:1402967694470418594>",
    "cười lên": "<:akiethumb:1488224506714525747>",
    "lên tòa": "<:akiethumb:1488224506714525747>",
    "anh co tu tin minh win khong": "💔",
    "nin di, phien ac": "<:akiethumb:1488224506714525747>",
    "lai lupin thu 3???": "<:arisu_cry:1497613253465866360>",
    "Dau tien la tha 5 ty qua ten lua vao Ukraine, sau do tan cong toan dien theo 2 huong Nga va Belarus nham nghien nat chinh phu Ukraine. Sau do dua quan tan cong Ba Lan, dong thoi su dung ten lua hat nhan de de doa chien luoc, ep NATO ko duoc dung kho ten lua hat nhan cua ho. Sau do chiem giu Romania de gianh lay nguon dau mo va cat dut an ninh nang luong chau au, roi nghien nat vung Baltic de tai xac nhap vao lien bang Nga. Sau do cu toan bo ham doi bien den va ham doi phuong bac danh phu dau Hoa Ky, tan cong vao Washington DC nham te liet kha nang chi huy toi cao. Rat co the se co kich ban phia Hoa Ky se dung B2 mang bom hat nhan nham ngan Nga chiem giu Lau Nam Goc. Chi can chiem giu Lau Nam Goc la co the tam thoi ngan My ho tro chau au, roi cu tan cong chau Au cho toi khi kiem soat toan bo dong au. Va the la xong.": "<:hlgotnonetosay:1402967694470418594>",
    "cất ngay cái tôi m vào": "<:khongphaisigmathinin:1320391737260245083>",
    "bớt ego đi": "<:khongphaisigmathinin:1320391737260245083>",
    "minh im lang la minh thang roi": "<:hlgotnonetosay:1402967694470418594>",
    "am nhac vuot qua loi noi": "<:hlgotnonetosay:1402967694470418594>",
    "Trong dàn thành viên Cỏ ba lá, Quạt khí độc là người mà ai cũng muốn tránh xa nhất, tại sao ư? Đối với Cỏ ba lá, câu ta là 1 người hôi hám. Đối với Cỏ dạ quang, cậu ta không thích sự xấu xí của Quạt khí độc. Đối với Cỏ nam châm, thì Quạt khí độc trông khá là vô dụng. Nhưng chỉ có Cỏ năm cánh thích thầm Quạt khí độc, vì cậu ta thích những thứ độc lạ từ chính Quạt khí độc nhất.": "<:fire_speaking:1477284820844544122>",
    "um um um um um um um um um um": "<:hlgotnonetosay:1402967694470418594>",
    "w ngulon ❤️‍🩹": "<:fire_speaking:1477284820844544122>",
    "aye chill ngulon <:fire_speaking:1477284820844544122>": "<:fire_speaking:1477284820844544122>",
    "aba": "<:tedoro:1491021720000266261>",
    "MA LỰC của GAME đang HỦY DIỆT NHÂN LOẠI": "<:fire_speaking:1477284820844544122>",
    "Dao nay ko con Hari cai ego cua ong cao bo me ra": "<:sad:1375060366442365029>",
    "the ma ho bao hari da bi ban": "<:sad:1375060366442365029>",
    "you arent kho ga enough": "<:hlgotnonetosay:1402967694470418594>",
    "<:hlgotnonetosay:1402967694470418594> Truoc tien la trien khai phao 155mm len khu vuc DBZ roi na phao nam san phang Seoul, roi sau do trien khai 1.5 trieu quan thong nhat ban dao va chien dau voi quan doi Han/My. Neu nhu ben do dam bat lai thi dung ten lua hat nhan nham thang vao Washington": "<:hlgotnonetosay:1402967694470418594>",
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