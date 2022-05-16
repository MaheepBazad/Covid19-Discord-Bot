import discord
from discord.ext import commands
import os

prefix = "!"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print("Ready!")
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey, {ctx.author.name}!")

for cog in os.listdir(f"D:\C C++\cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py','')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded")
            raise e

bot.run('OTc0NjMwNjQ2NTg2NzAzOTA0.G4AvzY.xKXCAkJAcRI1YNdF4RZsRtAa4hfK9yL6St-xWY')