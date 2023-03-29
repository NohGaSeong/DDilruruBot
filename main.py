import discord
from discord.ext import commands
from to import Token
import boto3

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def s3(ctx, *, text):
    if text == "보여줘":
        s3 = boto3.resource('s3')
        bucket_list = []

        for bucket in s3.buckets.all():
            bucket_list.append(bucket.name)

        await ctx.send(bucket_list)
    else :
        await ctx.send("말을 끝까지해줘")

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)





bot.run(Token)