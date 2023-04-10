from discord.ext import commands
from dotenv import load_dotenv
from commands.s3 import S3
from commands.ec2 import EC2
import discord
import os


load_dotenv()

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
token = os.getenv("TOKEN")


@bot.event
async def on_ready():
    await bot.add_cog(S3(bot))
    await bot.add_cog(EC2(bot))
    print(f"bot name : {bot.user.name}")
    print(f"bot id : {bot.user.id}")
    print(f"bot token : {token}")
    print('------')
    
if __name__ == "__main__":
    import sys

    if len(sys.args) > 1:

        token = sys.args[-1]
        try:
            bot.run(token)
        except Exception as e:
            raise e
        finally:
            sys.exit()
    else:
        bot.run(token)