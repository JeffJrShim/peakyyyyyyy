from redbot.core import commands

class MyFirstCog(commands.Cog):
    """My first cog on Red!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mocaishot(self, ctx):
        """Moca is hot."""
        # Your code will go here
        await ctx.send("I'm very hot. Get me bread please!")
