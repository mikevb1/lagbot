"""Cog for miscellaneous stuff."""

from collections import OrderedDict
import random

from discord.ext import commands
import asyncio

from .utils import *


class Misc:
    """Miscellaneous functions/commands and stuff."""

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot
        self.temote_prefix = ';'

    @commands.command(name='help')
    async def help_cmd(self, cmd=None):
        """Print this help."""
        if cmd is None:
            coms = OrderedDict()
            com_list = [
                'help', 'info', 'emotes', 'poke',
                'stream', 'join', 'leave', 'kick', 'ban']
            space = list_align(com_list, 2)
            for com in com_list:
                coms[com] = self.bot.commands[com]
            message = ['Available commands:', '```']
            for i, com in enumerate(coms):
                message.append('{}{}: {}'.format(
                    com, ' ' * space[i], coms[com].help.splitlines()[0]))
            message.append(
                '\nTo use Twitch/BTTV emotes, prefix the emote with {}'.format(
                    self.temote_prefix))
            message.append('```')
            message = '\n'.join(message)
            await self.bot.say(message)
        else:
            try:
                message = self.bot.commands[cmd].help.format(
                    self.bot.command_prefix)
            except KeyError:
                return
            except:
                message = self.bot.commands[cmd].help
            await self.bot.say('```' + message + '```')

    @commands.command()
    async def info(self):
        """Print bot information."""
        lib_link = \
            unformat_str('https://github.com/Rapptz/discord.py/tree/async')
        source_link = unformat_str('https://github.com/mikevb1/discordbot')
        twitch_emote_link = unformat_str('https://twitchemotes.com/')
        bttv_emote_link = unformat_str('http://www.nightdev.com/betterttv/')
        message = """This bot is written in Python using discord.py from {}
        The source code can be found at {}
        Global Twitch emote functionality provided by {}
        BTTV emote functionality provided by night (see code for API) {}""". \
            format(
                lib_link, source_link, twitch_emote_link, bttv_emote_link)
        await self.bot.say(message)

    @commands.command()
    async def poke(self):
        """Make sure bot is working."""
        replies = [
            'Hey!', 'Ow!', 'Stop that!', "I'm here!", 'I need an adult!']
        await self.bot.say(random.choice(replies))


def setup(bot):
    """'Magic' function to set up cog."""
    bot.add_cog(Misc(bot))