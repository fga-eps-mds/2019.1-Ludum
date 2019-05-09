
from rasa_core_sdk import Action
import json
import requests


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Mensagem enviada por uma custom action')
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


    
class ActionQuestion(Action):
    def name(self):
        return "action_question"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('"Espere jovem padawan, vou procurar uma resposta no StackOverflow para você"')
        except ValueError:
            dispatcher.utter_message(ValueError)
        try:
            link = requests.get('https://ludum-duvidas.herokuapp.com/api/duvidas')
            stack = json.loads(link.text)
            utterString = ''
            for i in range (0, len (stack['data'][0]['answer'])):
                utterString+= 'Resposta ' + str(i + 1) + '\n'
                utterString+= 'Titulo: ' + str(stack['data'][0]['answer'][i]['title']) + '\n'
                utterString+= 'Link: '  + str(stack['data'][0]['answer'][i]['link']) + '\n'
            dispatcher.utter_message(utterString)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
