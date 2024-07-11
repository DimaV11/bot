import discord
from discord.ext import commands
import random
import os 
import requests

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send('Я демонстративный бот!')

@bot.command('weather')
async def command_weather(ctx:commands.Context):
    await ctx.send('Погода сегодня класс!')

@bot.command('plus')
async def command_plus(ctx:commands.Context, a, b):
    a = int(a)
    b = int(b)
    result = a + b
    await ctx.send(result)

@bot.command('minus')
async def command_minus(ctx:commands.Context, a, b):
    a = int(a)
    b = int(b)
    result = a - b
    await ctx.send(result)

@bot.command('password')
async def command_password(ctx:commands.Context):
    sogl = 'qwrtpsdghjklxcvbnm'
    glas = 'eyuioa'
    numbers = '01234567890'
    symbol = '@#%?!'
    password = ""
    for i in range(4):
        password += random.choice(sogl)
        password += random.choice(glas)
    for i in range(2):
        password += random.choice(numbers)
    password += random.choice(symbol)
    print(password)

@bot.command('mem')
async def command_password(ctx:commands.Context):
    images = os.listdir('images')
    image_name = random.choice(images)
    with open('Images/'+image_name, 'rb') as file:
        image = discord.File(file)
    await ctx.send('Лови мемчик!', file=image)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
