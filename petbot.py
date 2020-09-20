"""
    Ethorbit's first bot, inspired by MoonlyDays' 
    TF2 Discord's Pet bot and uses their 
    image petting website's API
"""
import discord
import asyncio
import configparser
import requests

#Config
parser = configparser.ConfigParser()
parser.read('config.ini')
if (parser.has_section('MAIN')):
    mainConfig = parser['MAIN']
if (parser.has_option('MAIN', 'URL')):
    ConfigURL = mainConfig['URL']
else:
    ConfigURL = 'https://pet.moonlydays.com/pet.php'
if (parser.has_option('MAIN', 'URLParam')):
    ConfigURLParam = mainConfig['URLParam']
else:
    ConfigURLParam = 'remote'
if (parser.has_option('MAIN', 'Command')):
    ConfigCMD = mainConfig['Command']
else:
    ConfigCMD = 'pet'
if (parser.has_option('MAIN', 'CommandPresets')):
    ConfigCMDPresets = mainConfig['CommandPresets']
else:
    ConfigCMDPresets = ['?']

#Discord
async def isCommand(text):
    matchFound = False
    text = text.lower()
    for i in range(len(ConfigCMDPresets)):
        if (text.startswith(ConfigCMDPresets[i] + ConfigCMD)):
            matchFound = True  
            break
    return matchFound

client = discord.Client()

@client.event 
async def on_message(message):
    msg = message.content
    proceed = await isCommand(msg)
    if (proceed):
        atts = message.attachments
        mentions = message.mentions
        embeds = message.embeds

        async def petit(url):
            res = requests.get(ConfigURL, params={ConfigURLParam: url})
            await message.channel.send(res.url)

        if (len(atts) >= 1): # uploaded image
            await petit(str(atts[0].url))
        elif (len(embeds) >= 1): # website link
            await petit(str(embeds[0].url))
        elif (len(mentions) >= 1): # mentioned user's avatar
            await petit(str(mentions[0].avatar_url).replace('webp', 'png'))

if (parser.has_option('MAIN', 'Token')):
    client.run(mainConfig['Token'])
else:
    print("You need to create a config.ini in the same directory as the petbot.py, then you need to add ['MAIN'] and under it Token = <your bot token here>")