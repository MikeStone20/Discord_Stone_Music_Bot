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

client.run('OTg2NDA4MDg5Mzk1NzkzOTcy.GdQ04H.3FC9UodcWV71RkVSMDNFehCz5Wcsq_0Q35lHfE')