    # Import Bibl
import json
import discord
from discord.ext import commands
    #Token Your Bot
TOKEN = 'MTEzMDQzMTA2MTE2ODUwMDgwNw.G8rQbp.isWvTazzw68mbN0YLCSQQHCqDGb7fdUklI5elw'
    #Set Prefix And Intents
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
    #Info 
@bot.command()
async def info(ctx):
    await ctx.send('/github - Ссылка на мой GitHub аккаунт')
    await ctx.send('/discord - Ссылка на мой Discord сервер')
    #Link To My GitHub
@bot.command()
async def github(ctx):
    await ctx.send('GitHub - https://github.com/Fawzer')
    #Link Discord Server
@bot.command()
async def discord(ctx):
    await ctx.send('Discord Server  - https://discord.gg/48599aTPtF')
    #Kick Members
@bot.command()
async def kick(ctx, member: discord.Member, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} был кикнут с сервера.")
    else:
        await ctx.send("У вас нет разрешения на кик участников.")
    #Ban Members
@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} был забанен на сервере.")
    else:
        await ctx.send("У вас нет разрешения на бан участников.")
    #Clear Chat
@bot.command()
async def clear(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("У вас нет разрешения на очистку сообщений.")

bot.run(TOKEN)
