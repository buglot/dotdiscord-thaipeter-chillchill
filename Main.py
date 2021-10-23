import discord
import numpy as np
from discord import user
from discord import channel
from discord import guild
from discord.channel import VoiceChannel
from discord.utils import get
from discord.ext import commands



client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('Start!')
    print('Runing....')
    

@client.event
async def on_message(message):
    
    user_message = str(message.content)
    
    peter=['ควย','ปีเตอร์','buglot','peter','Peter','เตอร์']

    if message.author == client.user:
        return
    if user_message.lower() in peter:
        await message.channel.send("**ควย**  {0}:".format(message.author.mention))
        return
    if user_message.lower()=='ตาย':
        await message.channel.send(message.author.avatar_url)
    if user_message.lower() == 'รูปโปร':
        await message.channel.send(client.avatar_url)
        return
    if user_message.lower():
        try:
            a=float(eval(user_message))
            await message.channel.send("ได้ **{1}**    {0}:".format(message.author.mention,a))
        except:
            pass
    if user_message.lower().find('ลงตัว')!=0:
        try:
            a1,b1=user_message.lower().split("ลงตัว")
            c=[]
            k=0
            for x in range(1,int(b1)+1):
                if float(b1)%x==0:
                    c.append(str(x))
                    k+=1
            d=' '.join(c)
            await message.channel.send("{2} ตัว ได้ **{1}**    {0}:".format(message.author.mention,d,k))
        except:
           pass

    try:    
        playy,urll= user_message.split(" ")
    except:
        playy= user_message.lower().split(" ")[0]
    frd=['หาเพื่อน','.p','มาเล่นด้วยกัน']
    
    if playy in frd:
        channel = message.author.voice.channel
        try:

            voice = await channel.connect()
        except:
            pass
    elif playy == '.l':
        leave = get(client.voice_clients,guild=message.guild)
        if leave and leave.is_connected():
            await leave.disconnect()
            return
    await client.process_commands(message)
@client.command()
async def ครน(ctx,*,num):
    x=[int(x) for x in num.split()]
    c=np.lcm.reduce(x)
    await ctx.send(f'ครน คือ {c}    {ctx.author.mention}')

@client.command()
async def หรม(ctx,*,num):
    x=[int(x) for x in num.split()]
    c=np.gcd.reduce(x)
    await ctx.send(f'หรม คือ {c}    {ctx.author.mention}')

client.run('ODk3ODM2NjQ3MjI2NDI1MzQ1.YWbdiQ.yxPsNcTYOZPtYSSn0Q6AHnb5AV4')