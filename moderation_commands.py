import os
import discord
import random
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "j!")
master_id = 794952358613221376

@client.event
async def  on_message(message):
  if message.content.startswith('j! hello'):
    await message.channel.send('hi')
  if message.content.startswith(os.getenv('Master Code')):
    if message.author.id == master_id:
      await message.channel.send('master code activated')  
      await message.channel.send('rebooting bot...')
    else:
        channel = client.get_channel(937005307748560937)
        await channel.send(f'{message.author.mention} tried to use the master code <@794952358613221376>')
        await message.channel.send('oh piss off')
        await message.delete()
  if message.content.startswith('mping'):
    if message.author.id == master_id:
      await message.channel.send(message.content[6:len(message.content)])  
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
    else:
        await message.channel.send('Access Denied')
        await message.channel.send('Reason : You are not a master')
@client.command(ctx)
async def 8ball(ctx):
  if message.content.startswith('#8ball'):
      num = random.randint(1,3)
      if num == 1:
        embeddd = discord.Embed(
        title='',
		    description=f'Yes.',
		    color=0xff0000)
        await message.channel.send(embed=embeddd)
      if num == 2:
        embeddd = discord.Embed(
        title='',
		    description=f'Nope.',
		    color=0xff0000)
        await message.channel.send(embed=embeddd)
      if num == 3:
        embeddd = discord.Embed(
        title='',
		    description=f'maybe idk 😳',
		    color=0xff0000)
        await message.channel.send(embed=embeddd)
