import discord
from discord.ext import commands
import asyncio
import os
import random
from dotenv import load_dotenv

load_dotenv('.env.local')

TOKEN = os.getenv('TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '.')
CHANNEL_ID = int(os.getenv('CHANNEL_ID')) if os.getenv('CHANNEL_ID') else None
SPAM_MESSAGE = os.getenv('SPAM_MESSAGE', 'yo')
SPAM_AMOUNT = int(os.getenv('SPAM_AMOUNT', 5))
SPAM_DELAY = float(os.getenv('SPAM_DELAY', 1))
JITTER = 0.3

try:
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, self_bot=True, help_command=None)
except AttributeError:
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, self_bot=True, help_command=None)

spam_running = False

@bot.event
async def on_ready():
    print(f"✅ {bot.user}")

@bot.command()
async def spam_start(ctx):
    """Spams SPAM_AMOUNT messages to CHANNEL_ID"""
    global spam_running
    if spam_running:
        return
    
    if not CHANNEL_ID:
        print("❌ CHANNEL_ID not configured")
        return
    
    spam_running = True
    try:
        channel = await bot.fetch_channel(CHANNEL_ID)
        for i in range(SPAM_AMOUNT):
            if not spam_running:
                break
            await channel.send(SPAM_MESSAGE)
            await asyncio.sleep(SPAM_DELAY + random.uniform(0, JITTER))
    except Exception as e:
        print(f"❌ {e}")
    finally:
        spam_running = False

@bot.command()
async def spam_stop(ctx):
    """Stops spam"""
    global spam_running
    spam_running = False

if __name__ == "__main__":
    bot.run(TOKEN)

