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
async def kick(message):
  if message.content.startswith('$kick'):
      if message.author.guild_permissions.kick_members:
        await message.channel.send(f"You need the following permissions for this\n\033Kick Members")
        return
      if message.mentions:
        member = await message.guild.query_members(user_ids=message.mentions[0].id)
        await member[0].kick(reason='reason')
        memb = str(member[0])
        await message.channel.send(f"`{memb}` has been kicked from the server.")
      else:
          await message.channel.send("You must specify a user to kick!")
          return  
