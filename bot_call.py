# Bot Queen's Call - Ficar em Call
import discord
from discord.ext import commands
import json

# Carrega configurações
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['MTQ4NDM4NDc1MDY0MTg3MjkyNg.GPnhd5.aUYPCMhwsQOlKECOHuJm_jXQcPdHnbrNgF8OhM']

# Configura o bot
intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Quando o bot iniciar
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    print("Digite !entrar no chat do servidor para que eu entre na call!")

# Comando para o bot entrar na call onde você estiver
@bot.command()
async def entrar(ctx):
    if ctx.author.voice:
        canal = ctx.author.voice.channel
        await canal.connect()
        await ctx.send(f"Entrei na call: {canal.name}!")
    else:
        await ctx.send("Você precisa estar em um canal de voz primeiro!")

# Comando para desconectar
@bot.command()
async def sair(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Saindo da call!")
    else:
        await ctx.send("Não estou em nenhuma call!")

# Inicia o bot
bot.run(TOKEN)

