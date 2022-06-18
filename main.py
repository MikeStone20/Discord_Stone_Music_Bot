from dis import disco
import discord
from discord.ext import commands
#import youtube_dl
import os
from music_bot import Music_Bot

discord_bot = None
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print('bot online')
    discord_bot = Music_Bot()
    

@bot.command()
async def hello(ctx, *message):
    
    await ctx.send(message)

@bot.command()
async def play(ctx, *song):

    channel = ctx.author.voice.channel
    bot_channel_exist = False if ctx.voice_client == None else True

    vc = []

    if(not bot_channel_exist):
       vc = await channel.connect()
   
    if len(song) > 0:
        discord_bot.__add__(song[0])
    vc.play(discord.FFmpegPCMAudio(executable="C:\\Users\\micha\\Desktop\\ffmpeg\\bin", source='C:\\Users\\micha\\Desktop\\imagine_dragons.mp3'))
    #current_song = discord_bot.get_current_song()
    #bot.play(current_song.file_location)
  

# @bot.event
# async def on_message(message):

#     author = message.author
   
#     if(len(message.content) == 0 or author == bot.user or message.content[0] != '$'):
#         return
    
#     print(message)

#     command_and_args = message.content.split(' ')

#     if  command_and_args[0] == '$find meaning':
#         await message.channel.send("There is no meaning, only oblivion.")

#     if command_and_args[0] == '$play':
#         if len(command_and_args) > 1:
#             discord_bot.__add__(command_and_args[1])
#         next_song = discord_bot.get_next_song
        
bot.run('OTg2NDA4MDg5Mzk1NzkzOTcy.GY59QV.2Iuul3tKJI7X-2Zfpuv3hKBPpRzjWvQB0GDNKI')