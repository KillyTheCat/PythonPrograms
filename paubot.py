import random
from discord.ext.commands import Bot

BOT_PREFIX = ("Pau ","Pliz ")
TOKEN = "NTg4MjUxMTI5MTYzNTQ2NjM0.XQCaCQ.nXJEnvU5SdsNK4WCPll0Z1m2qxE"

client = Bot(command_prefix = BOT_PREFIX)

@client.command(name = '8ball',
				description = 'Answers a yes or no question.'
	)

async def eightball(context):
	possible_responses=[
			"No.",
			"Best not.",
			"That's a resounding no.",
			"Can't tell but you may try",
			"I am not sure but you may try",
			"I think you should try it, but maybe you shouldn't",
			"Go ahead, it's your day",
			"Definitely",
			"Sure, luck is in your favour today"
	]
	await client.say(random.choice(possible_responses))

async def hello():
	possible_responses=[
			"No speech englis but Hallo",
			"Konichiwa minasaaaaaaan",
			"Gand maraa bhenchod maine terese nai baat karni",
			"Hello! Have a nice day!",
			"I am gay but Hello!",
			"Fuck off"
	]
	await client.say(random.choice(possible_responses))


client.run(TOKEN)