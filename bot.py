import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
PREFIX = os.getenv("BOT_PREFIX")

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name=f"'{PREFIX}' as prefix")
    await bot.change_presence(activity=activity)
    print(f'{bot.user.name}#{bot.user.discriminator} is online!')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')

@bot.command()
async def mc(ctx, channel_id: int):
    voice_channel = bot.get_channel(channel_id)
    if not voice_channel:
        await ctx.send(":x:|I couldn't find a voice channel with that ID.")
        return
    num_users = len(voice_channel.members)
    num_bots = len([m for m in voice_channel.members if m.bot])
    num_humans = num_users - num_bots
    mc_embed = discord.Embed(description=f"There are **{num_humans} humans** and **{num_bots} bots** in **{voice_channel.name}**.", color=0x00ff00)
    await ctx.send(embed=mc_embed)



@bot.event
async def on_voice_state_update(member, before, after):
    if not member.bot and not after.channel and member.guild.voice_client and member.guild.voice_client.channel == before.channel:
        await member.guild.voice_client.move_to(before.channel)

bot.run(TOKEN)
