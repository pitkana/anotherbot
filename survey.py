import nextcord
import json

surveys = {}

try:
    f = open("data/surveys.json", "r")
    jsonString = f.read()
    surveys = json.loads(jsonString)
    f.close()
except FileNotFoundError:
    pass

def writeSurveys():
    f = open("data/surveys.json", "w")
    jsonString = json.dumps(surveys)
    f.write(jsonString)
    f.close()

def newSurvey(name: str):
    if name in surveys:
        return False
    else:
        surveys[name] = []
        writeSurveys()
        return True
    
def listSurveys():
    collect = ""
    for survey in surveys:
        collect += "-" + survey + "\n"
    return collect

def getSurveyOptions():
    options = []
    for survey in surveys:
        options.append(nextcord.SelectOption(label=survey))
    return options

def getSurveyResponses(survey: str):
    survey = surveys[survey]
    responseString = ""
    for response in survey:
        responseString += '"' + response + '"\n\n'
    return responseString

def addSurveyResponse(survey: str, response: str):
    if survey in surveys:
        surveys[survey].append(response)
        writeSurveys()
        return True
    else: 
        return False


class SurveyCreateModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Create Survey",
            timeout=5 * 60,  # 5 minutes
        )
        self.name = nextcord.ui.TextInput(
            label="Survey name",
            min_length=5,
            max_length=255
        )
        self.add_item(self.name)
    
    async def callback(self, interaction: nextcord.Interaction):
        if newSurvey(self.name.value):
            await interaction.send(f'Created new survey {self.name.value}!')
        else:
            await interaction.send("A survey with that name already exists!")
    
class SurveyResponseModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            title="Survey Response",
            timeout=5 * 60,
        )
        
        self.survey = nextcord.ui.TextInput(
            label="Enter the name of the survey",
            style=nextcord.TextInputStyle.paragraph,
        )
        self.add_item(self.survey)

        self.response = nextcord.ui.TextInput(
            label="Give your response to the survey",
            style=nextcord.TextInputStyle.paragraph,
        )
        self.add_item(self.response)

    async def callback(self, interaction: nextcord.Interaction):
        if addSurveyResponse(self.survey.value, self.response.value):
            await interaction.send("Response logged", ephemeral=True)
        else:
            await interaction.send("Survey not found", ephemeral=True)
