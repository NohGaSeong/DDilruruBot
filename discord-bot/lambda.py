# main.py 로 이름 변경 예정.

import discord
from discord.ext import commands
import boto3
from dotenv import load_dotenv
import os
import sys

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
load_dotenv()
Token = os.getenv('Token')

lambda_client = boto3.client('lambda')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(Token)




bot.run(Token)
