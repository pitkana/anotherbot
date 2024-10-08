import nextcord
from nextcord.ext import commands

import asyncio

print("Getting bot token...")
try:
    f = open("bot_token.txt", "r")
    bot_token = f.readline()
    f.close()
    print(f"Bot token of length {len(bot_token)} found")
except:
    print("Bot token not found. Ensure that you've saved the bot token in the root directory as bot_token.txt")
    
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
@bot.slash_command(description="Displays anotherbot help")
async def help(interaction: nextcord.Interaction):
    await interaction.send("There is no functionality.")
    
bot.run(bot_token)