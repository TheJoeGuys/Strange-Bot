import os
import discord
import random
import moderation_commands
import requests
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "j!")
master_id = ["794952358613221376",]
activity = discord.Activity(name="You",type=discord.ActivityType.watching)
banned_words = ['68141','5403']

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in a {0.user}'.format(client))

@client.event
async def  on_message(message):
  if message.author == client.user:
    return

#nuke the code when updated
  if message.content.startswith('j! hello'):
    await message.channel.send('hi')
  if message.content.startswith('j! intro'):
    await message.channel.send('Hello I am Joe Bot. I help Joe To Setup your server')
  if message.content.startswith('j! p'):
    await message.channel.send(os.getenv('P LINKS')
) 
  if message.content.startswith('j! invite'):
    await message.channel.send(os.getenv('INVITE')
    )
  if message.content.startswith('j! c'):
    await message.channel.send(os.getenv('C LINKS')
    )
  if message.content.startswith('joe who?'):
    await message.channel.send(os.getenv('answer')
    )
  if message.content.startswith('among us'):
    await message.channel.send(os.getenv('sus')
    )
  if message.content.startswith('nuke ping'):
    await message.author.send(os.getenv('nuke')
    )        
  if message.content.startswith('spam'):
    await message.channel.send(os.getenv('spam')
    )     
  if message.content.startswith('...............'):
    await message.channel.send('https://cdn.discordapp.com/attachments/814362660622958644/875756629960818808/hmm_huge.png')
  if message.content.startswith('..........'):
    if message.content.startswith('...........'):
      return
    else:
      await message.channel.send('https://cdn.discordapp.com/emojis/875732238304706571.png?v=1')
    #do you know how make it send a emoji byte (from:byte) yes
  if message.content.startswith('....'):
    await message.channel.send('https://cdn.discordapp.com/emojis/875732238304706571.png?size=64')
  if message.content.startswith('dammm'):
    await message.channel.send('https://tenor.com/view/hydro-dam-water-gif-10651901') 
  if message.content.startswith('zammm'):
    await message.channel.send('https://cdn.discordapp.com/attachments/862039010427142157/913375565283729428/unknown.png')    
  if message.content.startswith('hmmmm'):
    await message.channel.send('https://tenor.com/view/hmm-hmmm-hmmmm-thinking-gif-16016977')
  if message.content.startswith('*vsauce music playing*'):
    await message.channel.send('***hey vsauce micheal here***')
  if message.content.startswith("i'm back"):
    await message.channel.send("hi back i'm joe bot")
  if message.content.startswith("or is it"):
    await message.channel.send('*vsauce music playing*')      
  if message.content.startswith(';text'):
    if message.content.startswith(';text ;text'):
      return
    else:
      await message.channel.send(message.content[6:len(message.content)])
      await message.delete()
  if message.content.startswith('<@!644360160763969557>'):
    await message.channel.send('our boy diony is looking kinda sus, hes sus')
  if message.content.startswith(os.getenv('Master Code')):
    if message.author.id == master_id:
      await message.channel.send('master code activated')  
      await message.channel.send('rebooting bot...')
    else:
        channel = client.get_channel(937005307748560937)
        await channel.send('someone tried to use the master code <@794952358613221376>')
        await message.channel.send('oh piss off')
        await message.delete()
  if message.content.startswith('mping'):
    if message.author.id == master_id:
      await message.channel.send(message.content[6:len(message.content)])  
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
    if message.author.guild_permissions.administrator:
      await message.channel.send(message.content[6:len(message.content)])  
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])
      await message.channel.send(message.content[6:len(message.content)])   
    else:
        await message.channel.send('Access Denied')
        await message.channel.send('Reason : You are not a master or an admin')
  if message.content.startswith('drill'):
    try: await message.author.kick()
    
    except: await message.channel.send('Error: Cannot Kick member')
    await message.channel.send(f'{message.author.mention} got terminated for saying a banned word')
    await message.delete()
  if message.content.startswith('iwishtoleavethisserver'):
    if message.author.guild_permissions.ban_members:
      await message.channel.send(f'{message.author.name} wished to leave the server')
      await message.channel.send("until they forgot that they were a mod")
    else:  
     await message.channel.send(f'{message.author.name} wished to leave the server')
     try:
       invite = await message.channel.create_invite()
       await message.author.send(f'<a:TROLLED:927768935095500850>\ninvite: {invite}')
       await message.author.kick() 
     except: await message.channel.send("until he forgot that i don't have higher perms")
  if message.content in banned_words:
    await message.channel.send(f"{message.author.metion} Don't say that word")
    await message.delete()
  if message.content.startswith('$announce'):
    if message.author.guild_permissions.administrator:
      if message.guild.id == '862039010427142154':
        channel = client.get_channel(937287363737030696)
        try: await channel.send(message.content[6:len(message.content)])
        except: await message.channel.send("Error")
    if message.author.id in master_id:
      if message.guild.id == '862039010427142154':
        channel = client.get_channel(937287363737030696)
        await channel.send(message.content[6:len(message.content)])
    else:
         await message.channel.send("You need Administrator for this")


keep_alive()
client.run(os.getenv('TOKEN'))