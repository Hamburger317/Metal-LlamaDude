import os
import discord

DISCORD_API_KEY = os.environ.get("DISCORD_API_KEY")

bot = discord.Bot()

@bot.slash_command(description="")
async def ping(ctx):
    await ctx.respond(f"Pong: {bot.latency}")

bot.run(DISCORD_API_KEY)
