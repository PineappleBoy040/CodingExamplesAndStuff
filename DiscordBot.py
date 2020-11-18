import os
import random
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot Logged In As {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'pineapple for motherland':
        response = ("FOR MOTHERLAND!")
        await message.channel.send(response)
        await message.channel.send(file=discord.File('Sovjet.png'))
        await message.channel.send(file=discord.File('soviet-anthem.mp3'))

    if message.content == 'pineapple i did it':
        response = ("Good Job Buddy!")
        await message.channel.send(response)

    if message.content == 'pineapple i love you':
        response = ('I...Y-Yeah, nooo...')
        await message.channel.send(response)

    if message.content == 'pineapple':
        response = ("Heya Lovely!")
        await message.channel.send(response)

    if message.content == 'pineapple i need hugs':
        Auth = message.author
        response = ("*Pineapple Hugs " + (message.author.mention + "*"))
        await message.channel.send(response)

    if message.content == 'pineapple i need vodka':
        Auth = message.author
        response = ("*Pineapple Gives " + (message.author.mention + " Vodka* 'here you go!''"))
        await message.channel.send(response)
        await message.channel.send(file=discord.File('smirnoff.png'))

client.run('NjkwOTc5OTk0ODQyNjkzNjY1.XnZTRA.ZPmjMdm8gf0e2KmMKGElVlsrDOE')
