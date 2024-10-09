import nextcord
from nextcord.ext import commands

from survey import SurveyCreateModal, SurveyResponseModal, getSurveyResponses, listSurveys

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
    
@bot.slash_command()
async def help(interaction: nextcord.Interaction):
    """Displays anotherbot help.
    
    Parameters
    ----------
    interaction: Interaction
        The interaction object
    """
    await interaction.send("There is no functionality.")
    
@bot.slash_command()
async def survey(interaction: nextcord.Interaction):
    """
    Create, respond to and view anonymous surveys.
    
    Parameters
    ----------
    interaction: Interaction
        The interaction object
    """
    ...

@survey.subcommand()
async def create(interaction: nextcord.Interaction):
    """
    Create a new survey.
    
    Parameters
    ----------
    interaction: Interaction
        The interaction object
    """
    await interaction.response.send_modal(SurveyCreateModal())

@survey.subcommand()
async def respond(interaction: nextcord.Interaction):
    """
    Respond to a survey.
    
    Parameters
    ----------
    interaction: Interaction
        The interaction object
    """
    await interaction.response.send_modal(SurveyResponseModal())
    
@survey.subcommand()
async def display(interaction: nextcord.Interaction, survey: str):
    """
    View the responses for a survey.
    
    Parameters
    ----------
    interaction: Interaction
        The interaction object
    survey: str
        The survey to list the responses for
    """
    response = f"Responses for survey {survey}:\n\n"  + getSurveyResponses(survey)
    await interaction.send(response)

@survey.subcommand()
async def list(interaction: nextcord.Interaction):
    """
    List surveys currently added.

    Parameters
    ----------
    interaction: Interaction
        The interaction object
    """
    response = "Surveys:\n\n" + listSurveys()
    await interaction.send(response)
    
    
bot.run(bot_token)