import discord
from cogs.utils import config
from discord.ext import commands

extension = []

async def pre(bot, message):
    prefixes = []
    with open(f'cogs\prefixes.json') as file:
        data = json.load(file)
    if message.server.id in data:
        prefix = data[message.server.id]
    else:
        prefix = None

    if prefix is not None:
        prefixes.append(prefix)
        prefixes.append('&&')
        prefixes.append('<@468913182463885323> ')
        return prefixes
    if prefix is None:
        pass

async def token(bot, message):
    prefixes = []
    with open(f'cogs\prefixes.json') as file:
        data = json.load(file)
    if message.server.id in data:
        prefix = data[message.server.id]
    else:
        prefix = None

    if prefix is not None:
        prefixes.append(prefix)
        prefixes.append('&&')
        prefixes.append('<@468913182463885323> ')
        return prefixes
    if prefix is None:
        prefixes.append('&&')
        prefixes.append('<@468913182463885323> ')
        return prefixes

bot = commands.Bot(command_prefix=pre)


@bot.event
async def on_ready():
    print('\n\nLogged in as..')
    print(bot.user.name)
    print(bot.user.id)
    print('------\n\n')
    print('Hello!\n')
    print('I am connected on ' + str(len(bot.guilds)) + ' servers!')
    print('\n------')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    """Shuts bot down (owner-only)"""
    await ctx.send(":wave: C'ya!")
    await bot.logout()

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    """Loads module/cog"""
    try:
        bot.load_extension("cogs.{}".format(extension))
        print('\n\nMODULE LOAD\n[Cog loaded, {}.py]\n\n'.format(extension))
        await ctx.send("Module loaded.")
    except Exception as error:
        print('\n\nMODULE ERROR: {} was not loaded due to an error: \n[{}]\n\n'.format(extension, error))
        await ctx.send("There was an error loading that module. Check your console for more information.")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    """Unloads module/cog"""
    try:
        bot.unload_extension("cogs.{}".format(extension))
        print('\n\nMODULE UNLOAD\n[Cog unloaded, {}.py]\n\n'.format(extension))
        await ctx.send("Module unloaded.")
    except Exception as error:
        print('\n\nMODULE ERROR: {} was not unloaded due to an error: \n[{}]\n\n'.format(extension, error))
        await ctx.send("There was an error unloading that module. Check your console for more information.")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    """Reloads module/cog"""
    try:
        bot.unload_extension("cogs.{}".format(extension))
        bot.load_extension("cogs.{}".format(extension))
        print('\n\nMODULE RELOAD\n[Cog reloaded, {}.py]\n\n'.format(extension))
        await ctx.send("Module reloaded.")
    except Exception as error:
        print('\n\nMODULE ERROR: {} was not reloaded due to an error: \n[{}]\n\n'.format(extension, error))
        await ctx.send("There was an error reloading that module. Check your console for more information.")

if __name__ == '__main__':
    for extension in extension:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('\n\nMODULE ERROR: {} was not loaded due to an error: \n[{}]\n\n'.format(extension, error))

bot.run(token)
