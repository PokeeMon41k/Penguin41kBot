import discord
from discord.ext import commands

client = discord.Client(intents=discord.Intents().all())


channelDS = 873618780188704821

# Connect Bot

@client.event
async def on_ready():
    print ( 'BOT connected' )
    await client.change_presence( status = discord.Status.online, activity = discord.Game('Безмозглые'))


@client.event
async def on_member_join(member):
    channel = client.get_channel(channelDS)
    await channel.send(embed = discord.Embed(description = f'**Пингвинчик {member.mention}, наткнулся на нашу семейку!** 👋', colour = discord.Color.green()))

@client.event
async def on_member_remove(member):
    channel = client.get_channel(channelDS)
    await channel.send(embed = discord.Embed(description = f'**Пингвинчик ``{member},`` предал нас!** 💔', colour = discord.Color.red()))

token = 'ODc5NjMwMjI4OTE2NDIwNjcw.YSShfQ.Z4EZJut1S-TxT9jgzGxq03sV7Rw'
client.run(token)