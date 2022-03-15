import lightbulb
import hikari
import discord
from config import TOKEN

bot = lightbulb.BotApp(token=TOKEN,
                       default_enabled_guilds=(GUILD_ID_HERE)
                       )


@bot.command
@lightbulb.command('ping', "Reply's with pong")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Adds to values together.')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


bot.run()
