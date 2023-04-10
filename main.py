from discord.ext import commands
from dotenv import load_dotenv
from commands.s3 import S3
from commands.ec2 import EC2
import discord
import os


bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
load_dotenv()
token = os.getenv("TOKEN")


@bot.event
async def on_ready():
    await bot.add_cog(S3(bot))
    await bot.add_cog(EC2(bot))
    print(f"bot name : {bot.user.name}")
    print(f"bot id : {bot.user.id}")
    print(f"bot token : {token}")
    print('------')
    

bot.run(token)