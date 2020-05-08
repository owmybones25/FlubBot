import discord
import random
import requests
from botkey import *

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    num = random.randint(0,101)
    if message.content.startswith('$flube'):
        try:
            if (message.attachments[0].id > 0):
                url = message.attachments[0].url
                url = dreamer(10,url)
                await message.channel.send(url)
                await message.channel.send('FℲ... L˥... U∩... Bq...')
            else:
                await message.channel.send('FLUB... Error... Fluuuub... Try again but with the command as a caption to a photo Fluuuuuuuuuuuuuuuuuuuubbbb!!!')
        except IndexError:
            pass
    try:
        if(message.attachments[0].id > 0) and num > 95:
            url = message.attachments[0].url
            url = dreamer(4,url)
            await message.channel.send(url)
            await message.channel.send('FℲ... L˥... U∩... Bq...')
    except IndexError:
        pass
    if num >= 90:
        x = random.randint(0,14)
        if x == 0:
            msg = 'flub Flub FLUB?'
        elif x == 1:
            msg = 'fLuUuUuB?!?!?!?!'
        elif x == 2:
            msg = 'flub flub flub flub flub flub?'
        elif x == 3:
            msg = 'FLUB!'
        elif x == 4:
            msg = 'FLuB FlUB fluwb FLUB'
        elif x == 5:
            msg = 'Flub'
        elif x == 6:
            msg = 'flubber'
        elif x == 7:
            msg = 'flubbed'
        elif x == 8:
            msg = 'F̡̡̧̤͕̯̱̗̝͖̫͚̞͙͙͖̻̘̙̅͑ͣ͛̈̀ͅl̵̢̢͙͖͓̰̱̗͕̻̯͈͍̰͈̣̻̿ͥ̈́͛̈̎̌̐͜͝ͅữ̸̡̢̲̬̲̲̠̝̣͎͌̃ͨ̿̉ͦ̇̏̿̇͌͌̋̆ͮͫͩ̐͘b̸͎̜̼̌͂͑̃̍ͣͧͦ̐͂ͭ̿̆ͤͤͧ͘͘͘͜'
        elif x == 9:
            msg = 'flubted'
        elif x == 10:
            msg = 'F,L,U,B,'
        elif x == 11:
            msg = 'Flub me daddy'
        elif x == 12:
            msg = 'FFFFFFFFFLLLLLLLLLLLLLUUUUUUUUUUUBBBBBBBBBBB'
        elif x == 13:
            msg = 'f       l           u         b'
        else:
            msg = 'F... L... U... B...'
        await message.channel.send(msg)
      
def dreamer(num, url):
    print('dreaming...\n')
    for x in range(num):
        r = requests.post("https://api.deepai.org/api/deepdream",data={'image':url,},headers={'api-key':API_Key})
        responce = str(r.json())
        x = responce.find('output_url')
        url = ''
        for i in range(x+14,len(responce)-2):
            url += responce[i]
        return url
client.run(bot_token)

