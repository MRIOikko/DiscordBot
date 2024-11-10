'''import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
intents = discord.Intents.all()
intents.members = True
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ID = os.getenv('DISCORD_GUILDID')
#-------------------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(1042544647903391766) 
    await channel.send('Erm, what the sigma?')




@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message: {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

client.run(TOKEN)'''


