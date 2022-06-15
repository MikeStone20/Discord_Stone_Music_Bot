import discord
import youtube_dl
import os

client = discord.Client()

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello")

    if message.content.startswith('$find meaning'):
        await message.channel.send("There is no meaning, only oblivion.")

client.run(os.getenv('DISCORD_TOKEN'))