from discord.ext import commands

class S3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def s3(self, ctx):
        await ctx.send("Hello World!")

def setup(bot):
    bot.add_cog(S3(bot))