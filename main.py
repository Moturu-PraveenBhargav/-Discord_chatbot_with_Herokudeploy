import discord
import os
import requests
import json
import random
# from replit import db
# from keep_alive import keep_alive

client = discord.Client()
##Ja-Ma Token
# TOKEN ="OTQ3NTE3Mjg5NTk3NjUzMDEy.YhuaPQ.0_2ZrLL6-LoPeWxx1AsLsJLf6so"

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    msg = str(msg.lower())
    numb= ['on','tw','th','fo','fi','si','se','ei','ni','te']
    if msg in numb:
      # msg = str(msg.lower())
      index = numb.index(msg)
      if msg.startswith(numb[index]) : 
        l=[]
        for i in range(0,index+1):
            quote = get_quote()
            l.append(quote)
        await message.channel.send(l)

    if msg.startswith('Hi') or msg.startswith('hi'):
        await message.channel.send('Hi There!❤')
      
    if msg.startswith('Inspire') or msg.startswith('inspire') or msg.startswith('Quote') or msg.startswith('q'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('Help') or msg.startswith('help'):
        await message.channel.send("This chat bot has limited opertions (Viewing QUOTES) -Developed by Mannu for his Jaanu❤. If you want to get the quote in your bucket type the following cmds only:-\n1. Inspire, q, Quote \nFOR BATCH (Just type 'Numbers first two letters' in words)\n Eg:(one- on,\ttwo -tw,\tthree - th... till Ten only)\n\n2. [on, tw, th, fo, fi, si, se, ei, ni, te]) \n\nENJOY!!🕺💃")

    


client.run("OTQ3NTE3Mjg5NTk3NjUzMDEy.YhuaPQ.0_2ZrLL6-LoPeWxx1AsLsJLf6so")