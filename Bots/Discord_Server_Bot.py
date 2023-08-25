    # Импорт Библиотек
import discord
from discord.ext import commands
    # Токен Бота 
TOKEN = 'MTEzMDQzMTA2MTE2ODUwMDgwNw.GZu0Ao.ZsjM51NhIizaBVZoCoa9uYmGw-Jj-2e78g10hw'
    #Set Prefix And Intents
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
    # Функции 
    # Информация о создателе
@bot.command()
async def info(ctx):
    await ctx.send('/github - Ссылка на мой GitHub аккаунт')
    await ctx.send('/discord - Ссылка на мой Discord сервер')
    # Ссылка на GitHub 
@bot.command()
async def github(ctx):
    await ctx.send('GitHub - https://github.com/Fawzer')
    # Ссылка на Discord сервер 
@bot.command()
async def discord(ctx):
    await ctx.send('Discord Сервер  - https://discord.gg/48599aTPtF')
    # Удаление участиников с сервера
@bot.command()
async def kick(ctx, member: discord.Member, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} был кикнут с сервера.")
    else:
        await ctx.send("У вас нет разрешения на кик участников.")
    # Бан участников на сервере
@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} был забанен на сервере.")
    else:
        await ctx.send("У вас нет разрешения на бан участников.")
    # Очистка чата
@bot.command()
async def clear(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("У вас нет разрешения на очистку сообщений.")

bot.run(TOKEN)
