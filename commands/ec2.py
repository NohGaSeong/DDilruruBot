from discord.ext import commands

class EC2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ec2(self, ctx):
        await ctx.send("Hello World!")

def setup(bot):
    bot.add_cog(EC2(bot))