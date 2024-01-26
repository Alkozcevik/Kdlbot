import discord
from discord.ext import commands
import time
import random
import discord
from discord.ext import commands, tasks
import asyncio
import os
intents = discord.Intents.all()
intents.bans = True
intents.typing = False
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)
# Katılma mesajı gönderilecek kanal ID'si
katilma_kanal_id = 1191787127948718130  # Bu kanal ID'sini kendi kanalınıza göre değiştirin

# Bot hazır olduğunda çalışacak fonksiyon
@bot.event
async def on_ready():
    print(f'{bot.user} is ready to go!')

# Üye katıldığında çalışacak fonksiyon
@bot.event
async def on_member_join(member):
    # Katılma mesajı gönderilecek kanalı bul
    katilma_kanal = bot.get_channel(katilma_kanal_id)

    # Katılma kanalı bulunamazsa hata ver
    if not katilma_kanal:
        print('Katılma kanalı bulunamadı. Lütfen bot sahibiyle iletişime geçin.')
        return

    # Kullanıcıdan isim ve tur numarasını al
    await katilma_kanal.send(f'{member.mention} lütfen isminizi ve tur numaranızı (WhatsApp grup numaranızı) atar mısınız? Adminlerimiz Müsait Olunca Size Yazacaktır')

bot.run("MTIwMDQxNTA4NTM2MTkwMTYwOA.G3GAKj.k4l21VYr9YM1sujJyw2xJfBW6GoGUZsCQUY8ns")    