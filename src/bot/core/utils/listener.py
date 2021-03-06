from functools import wraps

import discord
from discord.ext import commands
from mgylabs.utils.config import CONFIG


def on_message():
    def deco(func):
        @wraps(func)
        async def outerfunc(*args, **kwargs):
            bot: commands.bot = args[0].bot
            message: discord.Message = args[1]

            if message.author == bot.user:
                return

            if (message.channel.type.value == 1) and (CONFIG.disabledPrivateChannel):
                return
            ctx = await bot.get_context(message)

            if ctx.valid:
                return

            return await func(*args, **kwargs)

        return outerfunc

    return deco
