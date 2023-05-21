import discord
import os
import requests
import json
import random
from GoogleNews import GoogleNews
import re
from datetime import date

# from replit import db
# from keep_alive import keep_alive
#intents = discord.Intents.default()
#intents.message_content = True
#client = discord.Client(intents=intents)
client = discord.Client()
##Ja-Ma Token
# TOKEN ="OTQ3NTE3Mjg5NTk3NjUzMDEy.G6FqBT.ngOaLHG3Be_ONEjXguDXXgocrZuDtdO6lMtK9I"


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


# def get_news(location):
# #     location = input("Enter your Location:\t")
#     googlenews = GoogleNews()
#     googlenews = GoogleNews(period = '7d')
#     # choose = input("")
#     googlenews.search(location)
#     result = googlenews.result()
#     return(result)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg= str(msg.lower())
    #Quote Condition
    numb = ['on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni', 'te']
    if msg in numb:  #CONDITION :1
        msg = str(msg.lower())
        index = numb.index(msg)
        if msg.startswith(numb[index]):
            l = []
            for i in range(0, index + 1):
                quote = get_quote()
                l.append(quote)
            await message.channel.send(l)

    #CONDITION 2 TO GET THE NEWS
    if str(msg.lower()) == "news":
        await message.channel.send(
            "Choose your Location(Pls prefix 'show-' to the location. Eg: show-india):"
        )

    msg = str(msg.lower())
    if msg[0:4] == 'show':
        today = date.today()
        today = today.strftime("%m/%d/%Y")
        lis = msg.split('-')[1]
        googlenews = GoogleNews()
        googlenews = GoogleNews(start=today, end=today)
        # choose = input("")
        googlenews.search(lis)
        result = googlenews.result()

        await message.channel.send(result)

    else:

        if msg.startswith('hi'):
            await message.channel.send('Hi There!')

        if msg.startswith('Inspire') or msg.startswith(
                'inspire') or msg.startswith('quote'):
            quote = get_quote()
            await message.channel.send(quote)

        if msg.startswith("help"):
            await message.channel.send(
                'This chat bot has limited opertions (Viewing QUOTES) -Developed by Mannu for his Jaanu❤. If you want to get the quote in your bucket type the following cmd only(1. Inspire \n2. [on, tw, th, fo, fi, si, se, ei, ni, te]) ENJOY!!'
            )


client.run(
    "OTQ3NTE3Mjg5NTk3NjUzMDEy.G6FqBT.ngOaLHG3Be_ONEjXguDXXgocrZuDtdO6lMtK9I")
