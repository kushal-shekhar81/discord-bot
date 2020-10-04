import discord
import os
from discord.ext.commands import Bot
from random import choice

disc = os.getenv('DISCORD_TOKEN')

bot = Bot("!")


with open('compliments.txt','r') as file:
    complimentList = list(file)

with open('jokes.txt','r') as joke:
    jokesList = list(joke)

def getCompliment():
    return choice(complimentList)

def getJoke():
    return choice(jokesList)

@bot.event
async def on_ready():
    print('Logged in')

@bot.event
async def on_message(message):
    print(message.author,message.content,message.channel)
    
    if message.content[0] != "!":
        if message.author != bot.user:
            await message.channel.send(str(message.content) + " " + str(message.author.mention) )
    
    
    await bot.process_commands(message)
    

@bot.command(pass_context=True)
async def compliment(ctx, member:discord.Member):
    membersList = ctx.message.guild.members
    print(membersList)
    complimentToSend = getCompliment()
    complimentToSend += member.mention
    await ctx.send(complimentToSend)

@bot.command(pass_context=True)
async def joke(ctx, member:discord.Member):
    jokeToSend = getJoke()
    jokeToSend += member.mention
    await ctx.send(jokeToSend)

bot.run('DISCORD_TOKEN')  

#Replace your bot token inside the (''), and run the program
