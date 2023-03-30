import discord
from discord.ext import commands
from to import Token
import boto3
import datetime

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

    # if text == "다운로드":
    #     s3 = boto3.client('s3')
    #     url = s3.generate_presigned_url(
    #         ClientMethod='get_object',
    #         Params={
    #             # 버킷이름
    #             'Bucket' : 'gaseong-bucket',
    #             # 파일 이름
    #             'Key' : "gaseong.jpg",
    #         },
    #         ExpiresIn=datetime.timedelta(seconds=30)
    #     )
    #     await ctx.send("아래 주소에서 다운 받아줘! 30초후면 닫히니까 빨리!\n" + url)

@bot.command()
async def ec2(ctx, *, text):
    if text == "생성" : 
        ec2 = boto3.resource('ec2')

        instances = ec2.create_instances(
            ImageId = "ami-03221589fd7c8f183",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="jnc-keypair"
        )
        
        await ctx.send("생성됐으니까 계정에 가서 확인해줘")

@bot.command()
async def 키페어(ctx, *,text):
    if text[:2] == "생성":
        ec2 = boto3.resource('ec2')
        new_keypair = ec2.create_key_pair(KeyName=text[3:])
        print(new_keypair)
        await ctx.send(str(new_keypair.key_material))

    if text[:2] == "삭제":
        ec2 = boto3.client('ec2')
        delete_keypair = ec2.delete_key_pair(KeyName=text[3:])
        print(delete_keypair)

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)





bot.run(Token)