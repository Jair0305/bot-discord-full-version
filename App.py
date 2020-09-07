import discord
from discord.ext import commands

#----Bot----

bot = commands.Bot(command_prefix = ".", description = "This is an command that say 'Diego es joto'")

#----commands----

"""
----Codigo de refencias----
	@bot.command()
		async def info(ctx):
		    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
		    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
		    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
		    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
		    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
		    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
		    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

		    await ctx.send(embed=embed)
---------------------------
"""

@bot.command()
async def ping(ctx):
	await ctx.send("pong")

@bot.command()
async def diego(ctx):
	await ctx.send("Diego es joto")

@bot.command()
async def joto(ctx, name = None):
	if name != None:
		await ctx.send(f"{name} es joto")
	else:
		await ctx.send("Diego es joto")

#----Event----

@bot.event
async def on_ready():
	print("Bot is ready")

#----Bot-run----

bot.run("NzUyMzczNDQyNDg5MzUyMzEz.X1WsXw.M1C0VKdjwwhPUoFZqzWHFuTIYuU")