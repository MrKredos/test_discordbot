from discord.ext import commands
import discord

#CHANGE TOKEN 
BOT_TOKEN = ""
CHANNEL_ID = 1203965753452269578

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("YO")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send ("YO")
    
@bot.command()
async def hello(ctx):
    await ctx.send("YO") 

bot.run(BOT_TOKEN)