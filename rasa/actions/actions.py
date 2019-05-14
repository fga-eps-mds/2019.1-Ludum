
from rasa_core_sdk import Action
import json
import requests
from rasa_core_sdk.events import SlotSet

class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        api = 'https://ludum-duvidas.herokuapp.com/api/duvidas'
        try:
            dispatcher.utter_message('Espere jovem padawan,' +
                                     'vou procurar uma resposta' +
                                     'no StackOverflow para você')
        except ValueError:
            dispatcher.utter_message(ValueError)
        try:
            link = requests.get(api)
            stack = json.loads(link.text)
            utterString = ''
            for i in range(0, len(stack['data'][0]['answer'])):
                utterString += 'Resposta ' + str(i + 1) + '\n'
                utterString += 'Titulo: '
                utterString += (str(stack['data'][0]['answer'][i]['title']))
                utterString += '\n'
                utterString += 'Link: '
                utterString += str(stack['data'][0]['answer'][i]['link'])
                utterString += '\n'
            dispatcher.utter_message(utterString)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []



class ActionQuestion(Action):
    def name(self):
        return "action_question"

    def run(self, dispatcher, tracker, domain):
        try :
            pergunta = str(tracker.get_slot('pergunta'))
            dispatcher.utter_message(pergunta)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
