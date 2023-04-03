import discord
from discord.ext import commands
import boto3
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
load_dotenv()
Token = os.getenv('Token')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(Token)

# S3 파트
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


# ec2 파트
@bot.command()
async def ec2(ctx, *, text):
    ec2 = boto3.resource('ec2', region_name = "ap-northeast-2")
    if text == "생성" : 
        instances = ec2.create_instances(
            ImageId = "ami-03221589fd7c8f183",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="jnc-keypair"
        )
        
        await ctx.send("생성됐으니까 계정에 가서 확인해줘")

    if text == "리스트":
        reservations = ec2.describe_instance(Filters=[
            {
                "Name" : "instance-state-name",
                "Values" : ["running"],
            }
        ]).get("Reservations")

        for reservation in reservations:
            for instance in reservation["instances"]:
                instance_id = instance["instanceId"]
                instance_type = instance["InstanceType"]
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
        await ctx.send(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")

    if text[:2] == "종료":
        response = ec2.terminate_instances(instanceIds=[text[3:]])
        await ctx.send(response + "잘 종료됐으니까 확인해봐.")

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