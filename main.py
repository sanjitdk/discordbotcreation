import discord 
import os
from dotenv import load_dotenv
load_dotenv()

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if(message.author == self.user):
            return
        if(message.content.startswith('Hello')):
            await message.channel.send(f'Hi there {message.author}!')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)