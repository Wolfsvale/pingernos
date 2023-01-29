from discord.ext import commands
from discord import Embed
from utils.utils import utils
class Privacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["policy", "pp"])
    async def privacy(self, ctx):
        embed = Embed()
        embed.description = f"{self.bot.user.name} saves a minimal amount of data to allow for its functionality. Full information about what is collected can be found on [W.I.P. bear with us]. For any concerns, Mail to soapy@cloudykingdom.com"
        embed.color = utils.colors.blue
        await ctx.reply(embed=embed)

        
def setup(bot):
    bot.add_cog(Privacy(bot))