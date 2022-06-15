import discord
import youtube_dl
import os
from music_bot import Music_Bot

discord_bot = Music_Bot()
client = discord.Client()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):

    author = message.author

    if(len(message.content) == 0 or author == client.user or message.content[0] != '$'):
        return
    
    command_and_args = message.content.split(' ')

  
    
    if command_and_args[0] == '$hello':
        await message.channel.send("Hello")

    if  command_and_args[0] == '$find meaning':
        await message.channel.send("There is no meaning, only oblivion.")

    if command_and_args[0] == '$play':
        pass


client.run(os.getenv('DISCORD_TOKEN'))