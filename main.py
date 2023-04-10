from discord.ext import commands
from dotenv import load_dotenv
from commands.s3 import S3
from commands.ec2 import EC2
import discord
import sys
import os


load_dotenv()

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
token = os.getenv("TOKEN")


@bot.event
async def on_ready():

    if len(sys.argv) > 1:
        sys.exit()

    await bot.add_cog(S3(bot))
    await bot.add_cog(EC2(bot))
    print(f"bot name : {bot.user.name}")
    print(f"bot id : {bot.user.id}")
    print(f"bot token : {token}")
    print('------')
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        token = sys.argv[-1]
        bot.run(token)
    else:
        bot.run(token)