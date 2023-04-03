import discord
from discord.ext import commands
import boto3
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv('Token')

def test():
    if Token is not None:
        return True
    else :
        return False
