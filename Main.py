import discord
from asyncio import sleep
from discord.ext import commands
from discord.ext.commands import has_permissions, Bot

token = 'NzI5Mzk5NjQzMjM0MTA3NTQ0.XwIcgA.lE3yk5KuKpCDgAzGpuSa-O25v8A'

bot = commands.Bot(command_prefix='pk ')

@bot.event
async def on_ready():
    print('O PAI TA ON')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('You Leigo ? Este comando não existe !')    
    
@bot.event
async def on_message(message):
    print(message)

    msg = f'{message.content}'
    msg = msg.lower()

    if msg == 'ping':
        await message.channel.send('pong')
        
    if msg == 'pkapa':
        await message.channel.send('O PKAPA É UM MONSTRO, INSUBSTITUÍVEL EU DIRIA...')

    await bot.process_commands(message)

@bot.command()
async def limpar(ctx):
    await ctx.channel.purge(limit=20)
    
    await sleep(1.2)
    await ctx.send ('Apagado com sucesso !')

@bot.command()
async def falar(ctx, *,msg):
    await ctx.channel.purge(limit=1)
    await ctx.send (msg)


bot.run(token)
