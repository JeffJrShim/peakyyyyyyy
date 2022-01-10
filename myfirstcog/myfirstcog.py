from redbot.core import commands

class MyFirstCog(commands.Cog):
    """My first cog on Red!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mocaishot(self, ctx):
        """Moca is hot."""
        await ctx.send("I'm very hot. Get me bread please!")
    @commands.command(hidden=True)
    async def peakytime(self,ctx):
        """peaky time"""
        await ctx.send("I want to marry Peaky, like right now.")
