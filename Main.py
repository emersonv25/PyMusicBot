import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

token = '' # TOKEN AQUI
#client = commands.Bot(command_prefix='pk ')
bot = commands.Bot(command_prefix='pk ')
#players = {}
#COR = 0xF7FE2E

# AO FICAR ONLINE EXECUTA ESTÁ FUNÇÃO
@bot.event
async def on_ready():
    print('O DJ TA ON')

# comandos aleatorios -----------
@bot.command()
async def falar(ctx, *,msg):
    await ctx.channel.purge(limit=1)
    await ctx.send (msg)

# CONECTA NO CANAL DE VOZ
@bot.command(pass_context=True, brief="Faz o bot entrar no seu canal", aliases=['j', 'jo', 'entrar'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("VOCÊ PRECISA ESTÁ EM UM CANAL DE VOZ, SUA MULA !")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"O DJ TA ON no canal de voz: {channel}")

# DESCONECTA DO CANAL DE VOZ
@bot.command(pass_context=True, brief="Faz o bot sair do seu canal", aliases=['l', 'le', 'lea', 'sair'])
async def leave(ctx):
    #channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("O DJ TA OFF")
    else:
        await ctx.send("NÃO PODE SAIR DE ONDE NÃO ENTROU, SUA ANTA !")

# DÁ PLAY A PARTIR DE UMA URL, BAIXA O MP3 E TOCA.
@bot.command(pass_context=True, brief="Tocara uma musica 'play [url]'", aliases=['pl', 'p', 'tocar'])
async def play(ctx, *,url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Aguarde o término da música atual ou use o comando 'skip'")
        return
    await ctx.send("Um momento amigo ! Colocando lenha no servidor para reproduzir a música!")
    print("Someone wants to play music let me get that ready for them...")
    
    
    voice = get(bot.voice_clients, guild=ctx.guild)
    
    ydl_opts = {
        'default_search': 'ytsearch',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #r = ydl.extract_info(url ,download=False)
        #r = ydl.extract_info(f"ytsearch:'{url}'", download=False)
        ydl.download([url])
        
        #print(str(url))
        #title = r["title"]
        #print(title)
        
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
    await ctx.send(f"SOLTA O SOM DJ:")

# PAUSA A MUSICA
@bot.command(pass_context=True, aliases=['pa', 'pau', 'pausar', 'parar'])
async def pause(ctx):
     
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Pausando a Musica")
    else:
        print("Music not playing failed pause")
        await ctx.send("Não pode pausar o que não está reproduzindo !")

# RESUME A MUSICA
@bot.command(pass_context=True, aliases=['r', 'res', 'resumir'])
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("The show must go on ! Musica despausada !")
    else:
        print("Music is not paused")
        await ctx.send("Não pode resumir se não tem nada pausado !")

# PARA E PULA A MUSICA
@bot.command(pass_context=True, aliases=['s', 'ski', 'pular'])
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    #queues.clear()

    if voice and voice.is_playing():
        print("Music skipped")
        voice.stop()
        await ctx.send("Music skipped")
    else:
        print("No music playing failed to skip")
        await ctx.send("Não pode parar ou pular sem está tocando uma musica !")



bot.run(token)
