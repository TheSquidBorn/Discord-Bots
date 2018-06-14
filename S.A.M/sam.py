import asyncio
import time
import urllib
import discord
from discord import Game
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

BOT_PREFIX = ("!")
f = open("token.txt", r)
token = f.read()
 
client = Bot(command_prefix=BOT_PREFIX)

@client.command(pass_context=True)
async def playing(ctx):
	game = ctx.message.content
	game = game.split(" ", 1)[1]
	await client.change_presence(game=Game(name=game))

@client.command(pass_context=True)
async def wiki(ctx):
	global wikiLi
	msg = ctx.message.content
	a = msg.split(" ", 1)[1]

	if is_number(a) & (wikiLi is not None):
		i = int(a) - 1
		url = wikiLi[i]
		url = url.div.a["href"]
		url = "https://en.wikipedia.org" + url
		browser.get(url)
		soup = BeautifulSoup(browser.page_source, "html.parser")
		t = soup.find_all("h1", {"id":"firstHeading"})
		title = "**" + t[0].text + "**"
		p = soup.find_all("div",{"class":"mw-parser-output"})[0]
		p = p.find_all("p")[0]
		text = p.text

		while True:
			n = 1
			foot = "[" + str(n) + "]"
			text = text.replace(foot, "")
			if text == text.replace(foot," "):
				break
			else:
				p = p.replace(foot,"")
				n += 1

		await client.say(title + "\n" + text)

	elif is_number(a) & (wikiLi is None):
		msg = "Wiki var does not contain anything, use the !wiki command again and pass a search query this time (!wiki (query))"
		await client.say(msg)

	else:
		url = "https://en.wikipedia.org/w/index.php?search=" + a + "&title=Special:Search&profile=default&fulltext=1"
		browser.get(url)
		soup = BeautifulSoup(browser.page_source, "html.parser")
		li = soup.find_all("ul", {"class":"mw-search-results"})[0]
		li = li.find_all("li")
		wikiLi = li
		msg = "```\n"
		for n in range(0, len(li)):
			msg += str(n + 1) + ". " + li[n].a.text + "\n"
		msg += "```"
		await client.say(msg)

@client.command(pass_context=True)
async def gif(ctx):
	q = ctx.message.content
	q = q.split(" ", 1)[1]
	q = "https://giphy.com/search/" + q
	browser.get(q)
	time.sleep(1)
	soup = BeautifulSoup(browser.page_source, "html.parser")
	giphy = soup
	try:
		img = soup.find_all("img",{"class":"_gifImage_1mf53_41 _gifLink_1mf53_51"})[0]
		await client.say(img["src"])
	except:
		await client.say("Found Nothing")

@client.command()
async def gtastatus():
	await client.say("On it!")
	print("Getting GTA Status")
	browser.get("https://support.rockstargames.com/hc/en-us/articles/200426246")
	time.sleep(5)
	soup = BeautifulSoup(browser.page_source, "html.parser")
 
	divs = soup.find_all("div",{"class":"item"})
 
	for n in range(0, len(divs)):
		divs[n] = divs[n].find_all("div")[1]

	msg = ("```\nRockstar Service Status\n\nPC       " + divs[0].text + "\nPS4      " + divs[1].text + "\nXBone    " + divs[2].text + "\nSClub    " + divs[3].text + "\nPS3      " + divs[4].text + "\nXbox360  " + divs[5].text + "```")
	await client.say(msg)

@client.command(pass_context=True)
async def ud(ctx):
	q = ctx.message.content.split(" ", 1)[1]
	url = "https://www.urbandictionary.com/define.php?term=" + q
	browser.get(url)
	soup = BeautifulSoup(browser.page_source, "html.parser")
	if len(soup.find_all("div",{"class":"shrug space"})) is 0:
		await client.say("Found Nothing")
	else:
		div = soup.find_all("div",{"class":"def-panel"})[0]
		title = div.find_all("div",{"class":"def-header"})[0]
		text = div.find_all("div",{"class":"meaning"})[0]
		example = div.find_all("div",{"class":"example"})[0]
		title = title.find_all("a")[0]
		title = "**" + title.text + "**\n"
		text = "" + text.text + "\n"
		example = "*" + example.text + "*"
		msg = title + text + example
		await client.say(msg)

@client.command(pass_context=True)
async def lfg(ctx):
	user = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name="Looking For Group")
	if role in [r for r in user.roles]:
		await client.remove_roles(user, role)
	else:
		await client.add_roles(user, role)

@client.command()
async def commands():
	f = open("help", "r")
	await client.say(f.read())

@client.command()
async def schema():
	await client.say("https://docs.google.com/spreadsheets/d/1sn_MEpd4uUoIqVAYdQm8qX4Lwrgn3N28rhhnAR0sWBU/edit?usp=sharing")

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="fair, playing pharah"))
	print("Logged in as " + client.user.name)

wikiLi = None

#options = Options()
#options.set_headless(headless=True)
browser = webdriver.Firefox() #firefox_options=options
client.run(TOKEN)