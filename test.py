from discord.ext import commands
import discord

#CHANGE TOKEN 
BOT_TOKEN = "MTIwMzk1ODE5Nzg1NDAxMTQ4NA.G0P-26.CtG9nytA_e7e7brSHhhL7U_lXX968PQTMYxkWc"
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