import discord
import exp_commands
from discord.ext import commands
from urllib import parse, request
from urllib.request import Request
import re
import asyncio
from bs4 import BeautifulSoup
import random

#----variables----

palabrasBlockeadas = ["porno","hentai","sexy", "sexo", "desnudo", "desnuda", "porn"]

#----Bot----

intents = discord.Intents(messages = True)

bot = commands.Bot(command_prefix = ".", description = "This is an command that say 'Diego es joto'", intents = intents)
client = discord.Client(intents = intents)

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
	embed = discord.Embed(title="Funciones del bot", description="Este bot es para mostrarte imagenes de google e insultar a gente", color=discord.Color.blue())
	embed.add_field(name="Comandos", value=exp_commands.newcommands)
	
	await ctx.send(embed = embed)

#comando para agregar y testear nuevas funciones 
@bot.command()
async def test(ctx, user: discord.User):
	print(user.id)
	await user.send("A")

@bot.command()
async def ppt(ctx):
	res = random.choice(["piedra","papel","tijeras"])
	await ctx.send(res)

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
async def ap (ctx, word: str=None):

	isAdd = False

	if word != None:
		for palabra in palabrasBlockeadas:
			if word == palabra:
				await ctx.send("La palabra ya fue censurada!!!")
				isAdd = True
				break

		if not isAdd:
			palabrasBlockeadas.append(word)
			embed = discord.Embed(title="Nueva palabra censurada:", color = discord.Color.red())
			embed.add_field(name = f"{word}", value = "Ahora esta palabra será censurada en la busqueda de imagenes")
			await ctx.send(embed=embed)

	else:
		await ctx.send("Agregue una palabra plis 🥺")

@bot.command()
async def ep (ctx, word: str=None):
	if word != None:
		try:	
			palabrasBlockeadas.remove(word)
			await ctx.send(f"La palabra {word} a sido removida")
		except Exception as e:
			print("palabra no encontrada")

@bot.command()
async def img(ctx, *, imgSearch):

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

if __name__ == "__main__":
	bot.run("")