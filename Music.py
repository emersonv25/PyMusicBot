import discord
from asyncio import sleep
from discord.ext import commands
from discord.ext.commands import has_permissions, Bot
from discord.voice_client import VoiceClient

token = 'NzI5Mzk5NjQzMjM0MTA3NTQ0.XwIcgA.lE3yk5KuKpCDgAzGpuSa-O25v8A'
bot = commands.Bot(command_prefix='pk ')
conectado = False


@bot.event
async def on_ready():
    print('O DJ TA ON')

@bot.command()
async def entrar(ctx):
    try:
        canal = ctx.author.voice.channel
        await canal.connect()
        await ctx.send('O DJ TA ON !')
    except (AttributeError, TypeError):
        await ctx.send('VOCÊ PRECISA ESTÁ EM UM CANAL DE VOZ, SUA MULA !')
    except Exception:
        await ctx.send('EU JÁ ESTOU DENTRO, SUA MULA !')
@bot.command()
async def sair(ctx):
    try:
        await ctx.voice_client.disconnect()
        await ctx.send ('O DJ TA OFF !')
    except (AttributeError, TypeError):
        await ctx.send('NÃO PODE SAIR DE ONDE NÃO ENTROU, SUA ANTA !')



bot.run(token)