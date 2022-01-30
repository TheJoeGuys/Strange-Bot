import os
import discord
import random
import moderation_commands as mod_cmds
import requests
import praw
import json
import asyncio
from discord import Color as color
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
reddit = praw.Reddit(client_id='N0xcvM8my6p3JGDkOJba6w',
                     client_secret=os.getenv('Reddit Token'),
                     user_agent='Richardson_1672', 
                     username='Richardson_1672')
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

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
            await message.channel.send(message.content[6:len(message.content)])
            await message.channel.send(message.content[6:len(message.content)])
            await message.channel.send(message.content[6:len(message.content)])
            await message.channel.send(message.content[6:len(message.content)])
            await message.channel.send(message.content[6:len(message.content)])
        else:
            await message.channel.send('Access Denied')
            await message.channel.send(
                'Reason : You are not a master or an admin')

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
        if user.guild_permissions.administrator:
            if message.guild.id == '862039010427142154':
                channel = client.get_channel(937287363737030696)
                try:
                    await channel.send(message.content[6:len(message.content)])
                except:
                    await message.channel.send("Error")
        if user.id in master_id:
            if message.guild.id == '862039010427142154':
                channel = client.get_channel(937287363737030696)
                await channel.send(message.content[6:len(message.content)])
        else:
            await message.channel.send("You need Administrator for this")

    if msg.startswith('$kick'):
        if user.guild_permissions.kick_members:
            if message.mentions:
                member = await message.guild.query_members(
                    user_ids=message.mentions[0].id)
                await member[0].kick(reason='reason')
                memb = str(member[0])
                await message.channel.send(
                    f"`{memb}` has been kicked from the server.")
            else:
                await message.channel.send("You must specify a user to kick.")
        else:
            await message.channel.send(
                f"You need the following permissions for this\n**Kick Members**"
            )

    if message.content.startswith('$ban'):
        if user.guild_permissions.ban_members:
            if message.mentions:
                member = await message.guild.query_members(
                    user_ids=message.mentions[0].id)
                await member[0].ban(reason=f'By {user}')
                memb = str(member[0])
                await message.channel.send(
                    f"`{memb}` has been banned from the server.")
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
        embed = discord.Embed(title="Avatar", color=color.Black)
        embed.set_image(url=avatar)
        embed.set_author(name=user.name, url=avatar)
        await msg_send(embed=embed)
    if msg.startswith('!hello'):
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
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

    if msg.startswith('$meme'):
      memes_submissions = reddit.subreddit('memes').hot()
      post_to_pick = random.randint(1, 10)
      for i in range(0, post_to_pick):
          submission = next(x for x in memes_submissions if not x.stickied)

      await msg_send(submission.url)

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
        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")


keep_alive()
client.run(os.getenv('TOKEN'))
