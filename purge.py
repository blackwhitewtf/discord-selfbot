import discord
from discord.ext import commands
import asyncio
import os
import random
from dotenv import load_dotenv

load_dotenv('.env.local')

TOKEN = os.getenv('TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '.')
PURGE_CHANNEL_ID = int(os.getenv('PURGE_CHANNEL_ID')) if os.getenv('PURGE_CHANNEL_ID') else None
PURGE_AMOUNT = int(os.getenv('PURGE_AMOUNT', 100)) if os.getenv('PURGE_AMOUNT') else 100
PURGE_DELAY = float(os.getenv('PURGE_DELAY') or 0.5)
JITTER = 0.3

try:
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, self_bot=True, help_command=None)
except AttributeError:
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, self_bot=True, help_command=None)

@bot.event
async def on_ready():
    print(f"✅ {bot.user}")

@bot.command()
async def purge_start(ctx):
    """Deletes PURGE_AMOUNT of own messages from PURGE_CHANNEL_ID"""
    if not PURGE_CHANNEL_ID:
        print("❌ PURGE_CHANNEL_ID not configured")
        return
    
    try:
        # Versuche zuerst als Channel, dann als User (für DMs)
        try:
            channel = await bot.fetch_channel(PURGE_CHANNEL_ID)
        except:
            user = await bot.fetch_user(PURGE_CHANNEL_ID)
            channel = user.dm_channel or await user.create_dm()
        
        messages = [msg async for msg in channel.history(limit=PURGE_AMOUNT)]
        own_messages = [msg for msg in messages if msg.author == bot.user]
        
        for message in own_messages:
            await message.delete()
            await asyncio.sleep(PURGE_DELAY + random.uniform(0, JITTER))
        print(f"✅ {len(own_messages)} Nachrichten gelöscht")
    except Exception as e:
        print(f"❌ {e}")

@bot.command()
async def purge_all_start(ctx):
    """Deletes PURGE_AMOUNT messages from PURGE_CHANNEL_ID (all users)"""
    if not PURGE_CHANNEL_ID:
        print("❌ PURGE_CHANNEL_ID not configured")
        return
    
    try:
        # Versuche zuerst als Channel, dann als User (für DMs)
        try:
            channel = await bot.fetch_channel(PURGE_CHANNEL_ID)
        except:
            user = await bot.fetch_user(PURGE_CHANNEL_ID)
            channel = user.dm_channel or await user.create_dm()
        
        deleted = 0
        async for message in channel.history(limit=PURGE_AMOUNT):
            await message.delete()
            deleted += 1
            await asyncio.sleep(PURGE_DELAY + random.uniform(0, JITTER))
        print(f"✅ {deleted} Nachrichten gelöscht")
    except Exception as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    bot.run(TOKEN)
