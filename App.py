import discord
from discord.ext import commands
from urllib import parse, request
from urllib.request import Request
import re
from bs4 import BeautifulSoup

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
async def i(ctx, *, imgSearch):

	pathURL = parse.urlencode({"q" : imgSearch})
	pathURL = f"https://www.google.com/search?{pathURL}&tbm=isch&ved=2ahUKEwj5v5yH0dfrAhVRbqwKHZCQA2kQ2-cCegQIABAA&o{pathURL}&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAELEDEEM6BAgAEENQoxJYqB9g4iBoAHAAeACAAcwCiAHQBZIBBzAuMS4xLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=c3ZWX7m6C9HcsQWQoY7IBg&bih=661&biw=1280&hl=es-419"
	#print(pathURL, end="\n\n")
	url = Request(pathURL, headers = {"User-Agent": "Mozilla/5.0"})
	
	html_res = request.urlopen(url)

	soup = BeautifulSoup(html_res, features="html.parser")

	patt = re.compile('src="(.*)".*/>')

	results = []
	for a in soup.find_all('img'):
	    path = re.findall(patt, str(a))[0]
	    results.append(path)

	#print(results)
	embed = discord.Embed(title=f"{ctx.guild.name}", description=f"{imgSearch}")
	embed.set_thumbnail(url=results[1])
	await ctx.send(embed=embed)

#comando para dar la informacion del bot y del grupo
@bot.command()
async def info(ctx):
	embed = discord.Embed(title="Funciones del bot", description="Este bot es para mostrarte imagens de google e insultar a gente", color=discord.Color.blue())
	embed.add_field(name="Comandos", value=".info\n.img 'nombre de la imagen' 'numero de la imagen'\n.joto '@nombre'")
	
	await ctx.send(embed = embed)

#comando para agregar y testear nuevas funciones 
@bot.command()
async def test(ctx, user: discord.User, *,msg: str = None):

	if msg == None:
		msg = "Chinga toda su puta perra madre"

	embed = discord.Embed(title="Este pana: ", color = discord.Color.gold())
	embed.add_field(name=f"{msg}", value = f"{user}")
	embed.set_thumbnail(url=user.avatar_url)

	await ctx.send(embed = embed)

#maldice a la persona etiquetada
@bot.command()
async def ctm(ctx, user: discord.User, *,msg: str = None):

	if msg == None:
		msg = "Chinga toda su reputisima perra madre"

	embed = discord.Embed(title="Este pana: ", color = discord.Color.gold())
	embed.add_field(name=f"{msg}", value = f"{user}")
	embed.set_thumbnail(url=user.avatar_url)

	await ctx.send(embed = embed)

@bot.command()
async def img(ctx, *, imgSearch):

	palabrasBlockeadas = ["porno","hentai","sexy", "sexo"]

	try:
		n = int(imgSearch[-2:])
		imgSearch = imgSearch[:-2]
	except Exception as e:
		n = 1

	for palabra in palabrasBlockeadas:
		imgSearch = imgSearch.replace(palabra, "icono de bloqueado")

	print(imgSearch)

	pathURL = parse.urlencode({"q" : imgSearch})

	pathURL = f"https://www.google.com/search?{pathURL}&tbm=isch&ved=2ahUKEwj5v5yH0dfrAhVRbqwKHZCQA2kQ2-cCegQIABAA&o{pathURL}&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAELEDEEM6BAgAEENQoxJYqB9g4iBoAHAAeACAAcwCiAHQBZIBBzAuMS4xLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=c3ZWX7m6C9HcsQWQoY7IBg&bih=661&biw=1280&hl=es-419"
	#print(pathURL, end="\n\n")
	url = Request(pathURL, headers = {"User-Agent": "Mozilla/5.0"})
	
	html_res = request.urlopen(url)

	soup = BeautifulSoup(html_res, features="html.parser")

	patt = re.compile('src="(.*)".*/>')

	results = []
	for a in soup.find_all('img'):
	    path = re.findall(patt, str(a))[0]
	    results.append(path)

	#print(results)
	await ctx.send(results[int(n)])

@bot.command()
async def ping(ctx):
	await ctx.send("pong")

@bot.command()
async def joto(ctx, name = None):
	if name != None:
		print(f"Get: joto {name}\nSend: {name} es joto")
		await ctx.send(f"{name} es joto")
	else:
		print("Get: joto\nSend: Diego es joto")
		await ctx.send("Diego es joto")

#----Event----

@bot.event
async def on_ready():
	print("Bot is ready")
	

#----Bot-run----

bot.run("NzUyMzczNDQyNDg5MzUyMzEz.X1WsXw.VS3g7Etv3bVcXXxNqOUsotYmAuA")