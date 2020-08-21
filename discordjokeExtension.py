import os
import ppt_to_powerpoint,requests
import discord,asyncio,json,random
from discord.ext import commands
from discord import File
import jokesupport
token = os.getenv("TOKEN")
print(token)
client = commands.Bot(command_prefix='.')
# @client.event
def convertandPRovide(r,name):
	with open(f'{name}.pdf', 'wb') as f:		
		f.write(r)
	ppt_to_powerpoint.convert(f"{name}.pdf")
def shamingP(name):
	a = [f"{name} agrees that flatearthers are gods of physics.","So how many dimensions do you see right now?",
	f'''
Engineers - Please Donot Move Coffee Machine It will change settings.
{name} - Please DO NOT observe coffee machine It will change qauntum states.''',
	f"{name} Believes Newton and his equation Gravity = Gm1m2/r2",
	f"Nah! {name} is Newton"
]

	return random.choice(a)
# @client.event
# async def on_message(message):
# 	channel = message.channel
#     await channel.send(message)
#     print('Bot Online.')

# def jokef():
	# url = "https://gofugly.in/api/sub_categories/23"
	# # ch = ["ACCHE BOL","DHARMIK GYAAN","FACTS"]
	# a  = get)(url)

	# p = json.loads(a.text)
	# randomn = random.randint(0,len(p["result"]))	
	# # print(p)
	# cchosen = p["result"][randomn].get("id")
	# a  = get(url)
	# print(joke)
	# return joke
def jokef():
	joke = jokesupport.get_random_joke()
	return joke

@client.command() 
async def joke(ctx):
	message = jokef()
	await ctx.send(message)
@client.command()
async def shame(ctx):
	if "peaky" in str(ctx.author).lower():
		await ctx.send("You are too stupid too shame anyone.")
	message = shamingP(ctx.author)
	await ctx.send(message)
@client.command()
async def ppt(ctx):
    attachment_url = ctx.message.attachments[0].url
    attachment_name = ctx.message.attachments[0].filename
    attachment_name = attachment_name.replace(".pdf","")
    print(attachment_name)
    file_request = requests.get(attachment_url)
    convertandPRovide(file_request.content,attachment_name)
    await ctx.send(file = File(rf"{attachment_name}.pptx"),content="Done.....")
    os.remove(f"{attachment_name}.pdf")	
    os.remove(f"{attachment_name}.pptx")	

client.run(token)
