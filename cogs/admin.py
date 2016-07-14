from discord.ext import commands
import discord


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, *, member: discord.Member):
        """Kick user from server if you have permission."""
        try:
            await self.bot.kick(member)
        except discord.Forbidden:
            await self.bot.say("I don't have permission to kick.")
        except discord.HTTPException:
            await self.bot.say('Kicking failed.')
        else:
            await self.bot.say('\U0001f44c')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, *, member: discord.Member):
        """Ban user from server if you have permission."""
        try:
            await self.bot.ban(member)
        except discord.Forbidden:
            await self.bot.say("I don't have permission to ban.")
        except discord.HTTPException:
            await self.bot.say('Banning failed.')
        else:
            await self.bot.say('\U0001f44c')


def setup(bot):
    """Magic function to set up cog."""
    bot.add_cog(Admin(bot))
