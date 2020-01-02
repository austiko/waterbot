import os
import discord
# import random
# import requests
# import json
from discord.ext import commands
token = os.environ["WATER_TOKEN"]
bot = commands.Bot(command_prefix='.')

bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

# This command had to stay here or else i am ready to kill the whole bot.
@bot.command()
async def help(ctx,command:str=None):
    '''Help command
    This command only include available extensions/cogs/categories, and
    '''
    if command is None:
        cognames = []
        for i in ctx.bot.commands:
            if i.cog_name not in cognames:
                cognames.append(i.cogname)
        out = "`"
        for i in cognames:
            out += f"{i}\n"
        out += "`"
        embed = discord.Embed(title="Waterbot Help",colour=0xfffbb)
        embed.add_field(name="Available modules of waterbot",value=out)
    else:
        await ctx.send("Not implemented yet.")


# Used extentions because why not.
cogs = [
    'exts.core',
    'exts.fun',
    'exts.utils',
    'exts.dev'
    ]
if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)

# Run the bot
bot.run(token)
