import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "🤖 Railway 机器人运行中！"

def run():
    app.run(host='0.0.0.0', port=3000)

def keep_alive():
    t = Thread(target=run)
    t.start()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'🎉 {bot.user} 在 Railway 上线成功！')

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Railway Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def hello(ctx):
    await ctx.send('👋 你好！我从 Railway 运行！')

keep_alive()
bot.run(os.environ['TOKEN'])
