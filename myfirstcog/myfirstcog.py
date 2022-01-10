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
        if ctx.author.id == 750325757024141392:
            await ctx.send("Oh... u- uh hii peaky.. ehehehehhe")
        else: 
            await ctx.send("Shh, don't tell peaky this. I really want to marry him so bad.\n I'll self destruct this message so he wont see it.", delete_after=3)
