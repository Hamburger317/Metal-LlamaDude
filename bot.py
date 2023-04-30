#!/usr/bin/python3

import os
import discord
import subprocess

import mllama.metalmath

tokentxt = open('token.txt', 'r')
TOKEN = (tokentxt.read())
tokentxt.close()

bot = discord.Bot()

@bot.slash_command(description="")
async def ping(ctx):
    await ctx.respond(f"Pong: {bot.latency}")

@bot.slash_command(description="Get neofetch output from host")
async def neofetch(ctx):
    neofetchOut = subprocess.getoutput("neofetch --stdout")
    await ctx.respond(neofetchOut)

bot.add_application_command(mllama.metalmath.math_commands)

bot.run(TOKEN)
