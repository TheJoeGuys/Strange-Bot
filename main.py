import os
import discord
import random
import praw
import asyncio
import pyjokes
import randfacts
import json
from discord.ext import commands
from keep_alive import keep_alive
from requests import get 

client = commands.Bot(command_prefix="j!")
master_id = ["794952358613221376",]
activity = discord.Activity(name="You", type=discord.ActivityType.watching)
banned_words = ['68141', '5403']
coinsides = ['Heads', 'Tails']
rate_amount = random.uniform(0.0, 100.0)
r = random.randint(1, 100)
joke = pyjokes.get_joke()
reddit = praw.Reddit(client_id='N0xcvM8my6p3JGDkOJba6w',
                     client_secret=os.getenv('Reddit Token'),
                     user_agent='Richardson_1672', 
                     username='Richardson_1672')
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
post_to_pick = random.randint(1,50)
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in a {0.user}'.format(client))



@client.event
async def on_message(message):
    user = message.author
    msg = message.content
    msg_send = message.channel.send
    if user == client.user:
        return
    if (user.bot):
        return


#nuke the code when updated
    if message.content.startswith('joe who?'):
        await message.channel.send('joe mama')
    if message.content.startswith('among us'):
        await message.channel.send('sus')
    if message.content.startswith('nuke ping'):
        await user.send(os.getenv('nuke'))
    if message.content.startswith('spam'):
        await message.channel.send(os.getenv('spam'))
    if message.content.startswith('...............'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/814362660622958644/875756629960818808/hmm_huge.png'
        )
    if message.content.startswith('..........'):
        if message.content.startswith('...........'):
            return
        else:
            await message.channel.send(
                'https://cdn.discordapp.com/emojis/875732238304706571.png?v=1')
        #do you know how make it send a emoji byte (from:byte) yes
    if message.content.startswith('....'):
        await message.channel.send(
            'https://cdn.discordapp.com/emojis/875732238304706571.png?size=64')
    if message.content.startswith('dammm'):
        await message.channel.send(
            'https://tenor.com/view/hydro-dam-water-gif-10651901')
    if message.content.startswith('zammm'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/862039010427142157/913375565283729428/unknown.png'
        )
    if message.content.startswith('hmmmm'):
        await message.channel.send(
            'https://tenor.com/view/hmm-hmmm-hmmmm-thinking-gif-16016977')
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
    if message.content.startswith(os.getenv('Master Code')):
        if user.id == master_id:
            await message.channel.send('master code activated')
            await message.channel.send('rebooting bot...')
        else:
            channel = client.get_channel(937005307748560937)
            await channel.send(
                'someone tried to use the master code <@794952358613221376>')
            await message.channel.send('oh piss off')
            await message.delete()
    if message.content.startswith('mping'):
      if user.id == master_id or user.guild_permissions.administrator:
        if message.mentions:
          await message.channel.send(message.content[6:len(message.content)])
          await message.channel.send(message.content[6:len(message.content)])
          await message.channel.send(message.content[6:len(message.content)])
          await message.channel.send(message.content[6:len(message.content)])
          await message.channel.send(message.content[6:len(message.content)])
        else:
            await message.channel.send('Access Denied')
            await message.channel.send('Reason : You are not a master or an admin')

    if message.content.startswith('iwishtoleavethisserver'):
        if user.guild_permissions.ban_members:
            await message.channel.send(
                f'{user.name} wished to leave the server')
            await message.channel.send("until they forgot that they were a mod"
                                       )
        else:
            await message.channel.send(
                f'{user.name} wished to leave the server')
            try:
                invite = await message.channel.create_invite()
                await user.send(
                    f'<a:TROLLED:927768935095500850>\ninvite: {invite}')
                await user.kick(reason='He wished for it')
            except:
                await message.channel.send(
                    "until he forgot that i don't have higher perms")

    if message.content in banned_words:
        await message.channel.send(f"{user.metion} Don't say that word")
        await message.delete()

    if message.content.startswith('$announce'):
        if user.guild_permissions.administrator or user.id in master_id:
            if message.guild.id == '862039010427142154':
                channel = client.get_channel(937287363737030696)
                try:
                    await channel.send(message.content[6:len(message.content)])
                except Exception as e:
                    await msg_send(e)
            else:
              await msg_send('this is a exclucive command')
        else:
            await message.channel.send("You need Administrator for this")

    if msg.startswith('$kick'):
        if user.guild_permissions.kick_members:
            if message.mentions:
                member = await message.guild.query_members(user_ids=message.mentions[0].id)
                try:
                    await member[0].kick(reason=f'By {user}')
                    memb = str(member[0])
                    await message.channel.send(
                        f"`{memb}` has been kick from the server.")
                except Exception as e:
                     await msg_send(e)
            else:
                await message.channel.send("You must specify a user to kick.")
        else:
            await message.channel.send(
                f"You need the following permissions for this\n**Kick Members**"
            )

    if message.content.startswith('$ban'):
        if user.guild_permissions.ban_members:
            if message.mentions:
                member = await message.guild.query_members(user_ids=message.mentions[0].id)
                try:
                    await member[0].ban(reason=f'By {user}')
                    memb = str(member[0])
                    await message.channel.send(
                        f"`{memb}` has been banned from the server.")
                except Exception as e:
                     await msg_send(e)
            else:
                await message.channel.send("You must specify a user to ban!")
        else:
            await message.channel.send(
                f"You need the following permissions for this\n**Ban Members**",
                delete_after=5)
    '''if message.content.startswith('$muted'):
    if user.guild_permissions.timeout_members:
      role = discord.utils.get(guild.roles, name="Muted")
      await user.add_roles(role)
      await message.channl.send(f'')
    else:
      await message.channl.send(f'')'''

    if msg.startswith('$avatar'):
        avatar = user.avatar_url
        random_color = random.choice(colors)
        embed = discord.Embed(title="Avatar", color=random_color)
        embed.set_image(url=avatar)
        embed.set_author(name=user.display_name, url=avatar)
        await msg_send(embed=embed)
    if msg.startswith('!hello'):
        embed = discord.Embed(title="Title", description="Desc", color=random_color)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await msg_send(embed=embed)

    if message.content.startswith('$purge'):
        if user.guild_permissions.administrator is False:
            await message.channel.send(
                "You don't have the permissions to run this command.", delete_after=5)
            await message.delete()
            return
        lim = msg[7:len(message.content)]
        lim = int(lim)
        lim += 1
        limstr = str(lim - 1)
        if lim < 99 and msg != "":
            await message.channel.purge(limit=lim)
            await msg_send(f"{user.name} purged {limstr} messages.", delete_after=5)
        if lim > 99:
            await msg_send("The purge value cannot be greater than 98.", delete_after=5)

    if msg.startswith('$pyjoke'):
      await msg_send(pyjokes.get_joke())

    if msg.startswith('$snipe'): 
      if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")
      else:
          embed = discord.Embed(description=f"{snipe_message_content}")
          embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
          embed.set_author(name= f"<@{snipe_message_author}>")
          await message.channel.send(embed=embed)
    if msg.startswith('$coinflip'):
      await msg_send(f"**{user.name}** flipped a coin and got **{random.choice(coinsides)}**.")
    if msg.startswith('$rate'):
      await msg_send(f"I say `{msg[6:len(message.content)]}` are a good **{round(rate_amount, 4)} / 100**.")
    if msg.startswith('$hot'):
        hot = r / 1.17
        emoji = "💔"
        if int(hot) > 25:
            emoji = "❤"
        if int(hot) > 50:
            emoji = "💖"
        if int(hot) > 75:
            emoji = "💞"
        await msg_send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")
    
    if msg.startswith('$nickname'):
      if  user.guild_permissions.manage_nicknames:
        name = msg[6:len(message.content)]
        try:
            await member.edit(nick=name, reason=f'By {user.name}')
            message = f"Changed **{member.name}'s** nickname to **{name}**"
            if name is None:
                message = f"Reset **{member.name}'s** nickname"
            await msg_send(message)
        except Exception as e:
            await msg_send(e)
    if msg.endswith('!'):
      if message.channel.id == 889309445887250443:
        if msg[-2:-1] == 5:
          user = member.mention
          role = discord.utils.get(user.guild.roles, name="Test")
          await client.add_roles(user, role)
    if msg.startswith('$joinedat'):
        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.description = f'**{user}** joined **{message.guild.name}**\n{(user.joined_at)}'
        await msg_send(embed=embed)
    if message.content.startswith('#help'):
      await asyncio.sleep(0.5)
      
      embed = discord.Embed(
        title='**Joe Bot Commands**',
		    description=f'\n\n *__$help__* \n\n *__$embed <embed text goes here>__* \n\n *__#say <message goes here>__* \n\n *__#8ball <question>__* \n\n *__#waifu__* \n\n *__#purge <number>__ (number cant be above 98)* \n\n *__#kick <@user>__* \n\n**ENJOY!**',
		    color=random_color)
      await message.channel.send(embed=embed)
    if msg.startswith('$fact'):
      random_color = random.choice(colors)
      facts = randfacts.get_fact()
      embed = discord.Embed(title="Facts", description=facts, color=random_color)
      embed.set_footer(text=f"Requested By {user}", icon_url=user.avatar_url)
      await msg_send(embed=embed)
    if msg.startswith('$8ball'):
      random_color = random.choice(colors)
      question = msg[7:len(message.content)]
      response = random.choice(responses)
      embed=discord.Embed(title="Magic 8 Ball", color=random_color)
      embed.add_field(name=':8ball:Question: ', value=f'{question}', inline=True)
      embed.add_field(name=':8ball:Answer: ', value=f'{response}', inline=False)
      await msg_send(embed=embed)
      
      
keep_alive()
client.run(os.getenv('TOKEN'))